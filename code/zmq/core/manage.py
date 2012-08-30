__metaclass__ = type

import zmq


class ImageMessage:
    def __init__(self, width, length, row, column, image):
        self.width = width
        self.length = length
        self.row = row
        self.column = column
        self.image = image

    def dump(self):
        """Dump the image to text mode
        """

    @classmethod
    def load(cls, image_text):
        """Load the image from text
        """
        


def main():
    context = zmq.Context()
    # use a push pull socket for the workers


if __name__ == '__main__':
    main()
