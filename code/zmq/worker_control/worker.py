import zmq

from proto import control_recv, task_recv


def worker():
    control = zmq.Poller()
    control.register(self.task_socket, zmq.POLLIN)
    control.register(self.control_socket, zmq.POLLIN)
    # another possible way to do this is to use recv(zmq.NOBLOCK),
    # as shown in http://zguide.zeromq.org/py:msreader

    while True:
        # TODO: handle zmq.ZMQError if needed
        socks = dict(control.poll())
        # first check the control socket and then the task socket,
        # a signal received while doing a task would only take
        # effect during the next loop cycle
        if socks.get(self.control_socket) == zmq.POLLIN:
            msg = self.control_socket.recv()
            self._handle_control(msg)

        if socks.get(self.task_socket) == zmq.POLLIN:
            job = self.task_socket.recv()
            self._handle_job(job)


if __name__ == '__main__':
    worker()
