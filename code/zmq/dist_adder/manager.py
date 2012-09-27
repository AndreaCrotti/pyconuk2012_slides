import argparse
import zmq
from math import ceil

from proto import TASK_ADDR, Task


def start_manager(length, sub_len):
    context = zmq.Context()
    print("Doing a distributed sum of an array %d long" % length)
    to_sum = range(length)

    task_send_sock = context.socket(zmq.PUSH)
    task_send_sock.bind(TASK_ADDR)
    sent, idx = 0, 0
    num_pkts = int(ceil(float(sent) / sub_len))

    while sent < num_pkts:
        start, end = idx, idx+sub_len
        print("Sending sub-array from %d to %d" % (start, end))
        task_msg = Task(to_sum[start:end]) 
        task_send_sock.send(task_msg.dump())
        sent += 1
        idx += sub_len

    print("Sent all the messages")

def parse_arguments():
    parser = argparse.ArgumentParser(description='start the manager')
    parser.add_argument('length', type=int, help='Length of the array to sum')
    parser.add_argument('sub_len', type=int, help='sub length of the array')

    return parser.parse_args()

if __name__ == '__main__':
    ns = parse_arguments()
    start_manager(ns.length, ns.sub_len)
