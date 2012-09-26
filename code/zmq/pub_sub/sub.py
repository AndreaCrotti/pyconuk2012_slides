import zmq
import sys

ADDR = 'tcp://127.0.0.1:9999'


def sub(idx):
    context = zmq.Context()
    sub_sock = context.socket(zmq.SUB)
    sub_sock.connect(ADDR)
    sub_sock.setsockopt(zmq.SUBSCRIBE, '')

    while True:
        msg = sub_sock.recv()
        print("Subscriber %d received message %s" % (idx, msg))
        sys.stdout.flush()


if __name__ == '__main__':
    sub(int(sys.argv[1]))
