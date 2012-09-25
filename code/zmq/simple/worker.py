import sys
import zmq

from proto import TASK_ADDR, RESULT_ADDR, Result, Task


def worker(idx):
    print("Starting worker %d" % idx)
    context = zmq.Context()
    res_send_sock = context.socket(zmq.PUB)
    res_send_sock.connect(RESULT_ADDR)

    task_recv_sock = context.socket(zmq.PULL)
    task_recv_sock.connect(TASK_ADDR)

    while True:
        task_msg = task_recv_sock.recv()
        subarray = Task.load(task_msg).subarray
        print("Doing amazing computation on an array %d long" % len(subarray))
        res = Result(idx, sum(subarray))
        res_send_sock.send(res.dump())


if __name__ == '__main__':
    worker(int(sys.argv[1]))
