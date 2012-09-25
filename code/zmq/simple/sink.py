import sys
import zmq

from proto import RESULT_ADDR, Result


def start_sink(limit):
    print("Starting sink process")
    context = zmq.Context()
    recv_sock = context.socket(zmq.SUB)
    recv_sock.setsockopt(zmq.SUBSCRIBE, '')
    recv_sock.bind(RESULT_ADDR)

    received = 0
    tot_sum = 0

    while received < limit:
        res = Result.load(recv_sock.recv())
        print("Got result %s" % str(res))
        received += 1
        tot_sum += res.result

    print("Total sum = %d" % tot_sum)


if __name__ == '__main__':
    start_sink(int(sys.argv[1]))
