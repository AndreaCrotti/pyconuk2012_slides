import zmq

from multiprocessing import Process


def start_client():
    context = zmq.Context()
    sock = context.socket(zmq.REQ)
    while True:
        sock.send("Hello server")
        ans = sock.recv()
        print(ans)


def start_server():
    context = zmq.Context()
    sock = context.socket(zmq.REP)
    while True:
        req = sock.recv()
        print(req)
        sock.send("Hello client")


if __name__ == '__main__':
    Process(target=start_server).start()
    Process(target=start_client).start()
