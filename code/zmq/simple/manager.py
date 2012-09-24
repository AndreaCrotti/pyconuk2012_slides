import sys
import zmq

from proto import TASK_ADDR, Task


def manager(length, workers):
    context = zmq.Context()
    print("Doing a distributed sum of an array %d long" % length)
    to_sum = range(length)
    step = length / workers

    task_send_sock = context.socket(zmq.PUSH)
    task_send_sock.bind(TASK_ADDR)
    sent = 0
    idx = 0

    while sent < workers:
        task_msg = Task(to_sum[idx:idx+step])
        task_send_sock.send(task_msg.dump())
        sent += 1

    print("Sent all the messages")

if __name__ == '__main__':
    length, n_workers = map(int, sys.argv[1:])
    manager(length, n_workers)
