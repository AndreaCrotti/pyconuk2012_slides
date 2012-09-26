DELIMITER = '::'

TASK_ADDR = 'tcp://127.0.0.1:5559'
RESULT_ADDR = 'tcp://127.0.0.1:5560'


class Result:
    def __init__(self, idx, result):
        self.idx = idx
        self.result = result

    def __str__(self):
        return '%d --> %d' % (self.idx, self.result)

    def dump(self):
        return DELIMITER.join(map(str, [self.idx, self.result]))

    @classmethod
    def load(cls, msg):
        idx, result = msg.split(DELIMITER)
        return cls(int(idx), int(result))


class Task:
    def __init__(self, subarray):
        self.subarray = subarray

    def dump(self):
        return DELIMITER.join(map(str, self.subarray))

    @classmethod
    def load(cls, msg):
        subarray = map(int, msg.split(DELIMITER))
        return cls(subarray)
