import sys
import zmq

from time import sleep
from random import randrange

from proto import TASK_ADDR, RESULT_ADDR, Result, Task


def start_worker(idx):
    print("Starting worker %d" % idx)
    context = zmq.Context()
    res_send_sock = context.socket(zmq.PUB)
    res_send_sock.connect(RESULT_ADDR)

    task_recv_sock = context.socket(zmq.PULL)
    task_recv_sock.connect(TASK_ADDR)

    while True:
        task_msg = task_recv_sock.recv()
        subarray = Task.load(task_msg).subarray
        print("Worker %d doing amazing computation on an array %d long" % (idx, len(subarray)))
        res = Result(idx, sum(subarray))
        res_send_sock.send(res.dump())
        # TODO: check why we always get the same worker do the job
        sleep(randrange(5))


if __name__ == '__main__':
    start_worker(int(sys.argv[1]))
