__metaclass__ = type

from os import path

from PIL import Image

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


def dims_to_boxes(ncols, nrows, size):
    """Yield boxes to fill the given size with ncols and nrows,
    keeping the boxes as square as possible
    """
    


def size_to_rows_cols(dim, fields):
    """Yield tuples of coordinates from the number for rows and
    columns
    """
    step = dim / fields
    return range(0, dim, step)[:-1] + [dim-1]


class Splitter:
    """Split the image in many sub-images and send everything to the
    socket
    """
    def __init__(self, img_path, ncols, nrows):
        self.ncols = ncols
        self.nrows = nrows
        self.img = Image.open(open(img_path))

    def generate_pics(self, remove=False):
        pass



def main():
    context = zmq.Context()
    # use a push pull socket for the workers


if __name__ == '__main__':
    main()
