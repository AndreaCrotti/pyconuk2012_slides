import logging
import zmq
from time import sleep
from multiprocessing import Process

logger = logging.getLogger(__name__)

LOG_ADDR = 'tcp://127.0.0.1:7777'


def add_zmq_handler(root_logger):
    """Take a context and generate a ZMQ PUBHandler object adding it
    to the handlers
    """
    from zmq.log.handlers import PUBHandler
    zmq_handler = PUBHandler(LOG_ADDR)
    root_logger.addHandler(zmq_handler)


def setup_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    sh_handler = logging.StreamHandler()
    sh_handler.setFormatter(logging.Formatter())
    root_logger.addHandler(sh_handler)
    add_zmq_handler(root_logger)


def watch_log():
    context = zmq.Context()
    log_watcher = context.socket(zmq.SUB)
    log_watcher.connect(LOG_ADDR)
    log_watcher.setsockopt(zmq.SUBSCRIBE, '')

    while True:
        print("Log watcher: %s" % log_watcher.recv())


if __name__ == '__main__':
    # is this used anywhere??
    watch_log()
    # Process(target=watch_log).start()
    # sleep(1)
    # logger.info("This should go around")
