import sys

from os import fork, kill
from signal import SIGTERM

from worker import start_worker
from sink import start_sink
from manager import start_manager

LEN = 100000
WORKERS = 5
SUB_LEN = 100

def on_forked_process(func):
    """Decorator that forks the process, runs the function and gives
    back control to the main process
    """
    def _on_forked_process(*args, **kwargs):
        if fork() == 0:
            func(*args, **kwargs)
            sys.exit(0)

    return _on_forked_process


def main():
    pids = []
    sink = on_forked_process(start_sink)
    pids.append(sink(SUB_LEN))
    manager = on_forked_process(start_manager)
    pids.append(manager(LEN, WORKERS))
    for i in range(WORKERS):
        worker = on_forked_process(start_worker)
        pids.append(worker(i))

    # otherwise it will quit immediately
    while True: pass

    return pids

if __name__ == '__main__':
    pids = []
    try:
        pids = main()
    except KeyboardInterrupt:
        for pid in pids:
            print("Killing process %d" % pid)
            kill(pid, SIGTERM)
