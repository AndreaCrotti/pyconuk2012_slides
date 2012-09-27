import zmq
import sys

ADDR = 'tcp://127.0.0.1:9999'


def pull(idx):
    context = zmq.Context()
    pull_sock = context.socket(zmq.PULL)
    pull_sock.connect(ADDR)
    while True:
        msg = pull_sock.recv()
        print("Worker %d consumed %s" % (idx, msg))
        sys.stdout.flush()


if __name__ == '__main__':
    pull(int(sys.argv[1]))
