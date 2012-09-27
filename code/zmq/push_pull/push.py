from time import sleep
from itertools import count
import zmq

ADDR = 'tcp://127.0.0.1:9999'


def push():
    context = zmq.Context()
    push_sock = context.socket(zmq.PUSH)
    push_sock.bind(ADDR)
    for i in count(0):
        push_sock.send(str(i))
        sleep(2)

if __name__ == '__main__':
    push() 
