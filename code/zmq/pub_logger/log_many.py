import logging

from itertools import count
from time import sleep

from pub_log import setup_logging

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    setup_logging()
    for i in count(0):
        logger.info("Log message number %d" % i)
        sleep(1)
