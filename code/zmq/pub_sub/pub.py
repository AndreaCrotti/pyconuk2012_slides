from time import sleep
from itertools import count
import zmq

ADDR = 'tcp://127.0.0.1:9999'


def pub():
    context = zmq.Context()
    pub_sock = context.socket(zmq.PUB)
    pub_sock.bind(ADDR)

    for i in count(0):
        pub_sock.send(str(i))
        sleep(2)


if __name__ == '__main__':
    pub()
