import zmq
from multiprocessing import Process

TASK_ADDR = 'tcp:127.0.0.1:5555'
RESULT_ADDR = 'tcp:127.0.0.1:5556'


context = zmq.Context()
send_task = context.socket(zmq.PUSH)


class Sink:

    def run(self):
        pass


def main():
    pass

if __name__ == '__main__':
    main()
