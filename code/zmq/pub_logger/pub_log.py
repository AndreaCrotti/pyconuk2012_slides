import logging
import zmq


LOG_ADDR = 'tcp://127.0.0.1:7777'


def add_zmq_handler():
    """Take a context and generate a ZMQ PUBHandler object adding it
    to the handlers
    """
    from zmq.log.handlers import PUBHandler
    root = logging.getLogger()
    zmq_handler = PUBHandler(LOG_ADDR)
    root.addHandler(zmq_handler)


if __name__ == '__main__':
    context = zmq.Context()
    # is this used anywhere??
    add_zmq_handler()
