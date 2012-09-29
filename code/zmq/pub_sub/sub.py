import zmq
import sys

from proto import ADDR

# from proto import BACKEND_ADDR
# sub_sock.connect(BACKEND_ADDR)


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
