__metaclass__ = type

from os import path

import zmq

CUR_DIR = path.dirname(__file__)
IMAGE = path.join(CUR_DIR, 'zeromq.png')
DELIMITER = ';'
DATA_DEL = ':DATA_START:'


class ImageMessage:
    def __init__(self, width, length, row, column, image_path):
        self.width = width
        self.length = length
        self.row = row
        self.column = column
        self.image_path = image_path

    def __str__(self):
        return DELIMITER.join(map(str, [self.width, self.length, self.row, self.column, self.image_path]))

    def dump(self):
        """Dump the image to text mode
        """
        return DATA_DEL.join([str(self), open(self.image_path).read()])

    @classmethod
    def load(cls, image_text):
        """Load the image from text
        """
        fields, data = image_text.split(DATA_DEL)
        img = ImageMessage(*(fields.split(DELIMITER)))
        open(img.image_path + '.loaded', 'w').write(data)


def main():
    context = zmq.Context()
    # use a push pull socket for the workers


if __name__ == '__main__':
    main()
