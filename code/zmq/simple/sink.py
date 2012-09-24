import zmq

from .proto import RESULT_ADDR


def sink():
    context = zmq.Context()
    recv_sock = context.socket(zmq.SUB)
    recv_sock.setsockopts(zmq.SUBSCRIBE, '')
    recv_sock.bind(RESULT_ADDR)

    while True:
        res = recv_sock.recv()
        print("Got result %s" % res)


if __name__ == '__main__':
    main()
