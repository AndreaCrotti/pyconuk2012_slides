from itertools import count

import zmq


ADDR = 'tcp://127.0.0.1:10000'

def start_client():
    context = zmq.Context()
    sock = context.socket(zmq.REQ)
    # connect will not fail if the server is not listening!
    sock.connect(ADDR)

    for idx in count(0):
        sock.send("Hello %d" % idx)
        ans = sock.recv()
        print(ans)


if __name__ == '__main__':
    start_client()
