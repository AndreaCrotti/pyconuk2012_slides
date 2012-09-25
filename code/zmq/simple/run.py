from os import fork, kill
from signal import SIGTERM

from worker import worker
from sink import sink
from manager import manager

LEN = 100000
WORKERS = 50
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
    sink = on_forked_process(sink)
    pids.append(sink(SUB_LEN))
    pids.append(manager(LEN, WORKERS))
    manager = on_forked_process(manager)
    for i in range(WORKERS):
        worker = on_forked_process(worker)
        pids.append(worker(i))

    # otherwise it will quit immediately
    while True: pass

    return pids

if __name__ == '__main__':
    try:
        pids = main()
    except KeyboardInterrupt:
        for pid in pids:
            print("Killing process %d" % pid)
            kill(pid, SIGTERM)
