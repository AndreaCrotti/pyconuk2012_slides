import zmq

from proto import FRONTEND_ADDR, BACKEND_ADDR


def start_forwarder():
    print("Starting the forwarding")
    context = zmq.Context()
    frontend = context.socket(zmq.SUB)
    frontend.setsockopt(zmq.SUBSCRIBE, '')
    frontend.bind(FRONTEND_ADDR)
    backend =  context.socket(zmq.PUB)
    backend.bind(BACKEND_ADDR)
    zmq.device(zmq.FORWARDER, frontend, backend)


if __name__ == '__main__':
    start_forwarder()
