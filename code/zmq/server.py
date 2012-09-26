import zmq
from time import sleep

ADDR = 'tcp://127.0.0.1:10000'


def start_server():
    context = zmq.Context()
    sock = context.socket(zmq.REP)
    # bind has the same meaning
    sock.bind(ADDR)

    while True:
        req = sock.recv()
        print(req)
        sock.send("World")
        sleep(1)


if __name__ == '__main__':
    start_server()
