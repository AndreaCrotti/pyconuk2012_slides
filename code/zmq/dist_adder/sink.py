import argparse
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
        sys.stdout.flush()
        received += 1
        tot_sum += res.result
        print("Received %d packets" % received)

    print("Total sum = %d" % tot_sum)
    sys.stdout.flush()


def parse_arguments():
    parser = argparse.ArgumentParser(description='Start the sink process')
    parser.add_argument('num_pkts', help='number of packets to expect')

    return parser.parse_args()

if __name__ == '__main__':
    ns = parse_arguments()
    start_sink(ns.num_pkts)
