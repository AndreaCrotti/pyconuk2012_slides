import sys
import zmq

from proto import TASK_ADDR, Task


def start_manager(length, sub_len):
    context = zmq.Context()
    print("Doing a distributed sum of an array %d long" % length)
    to_sum = range(length)

    task_send_sock = context.socket(zmq.PUSH)
    task_send_sock.bind(TASK_ADDR)
    sent, idx = 0, 0

    while sent < sub_len:
        start, end = idx, idx+sub_len
        print("Sending sub-array from %d to %d" % (start, end))
        task_msg = Task(to_sum[start:end]) 
        task_send_sock.send(task_msg.dump())
        sent += 1
        # increment the index
        idx += sub_len

    print("Sent all the messages")

if __name__ == '__main__':
    length, sub_len = map(int, sys.argv[1:])
    start_manager(length, sub_len)
