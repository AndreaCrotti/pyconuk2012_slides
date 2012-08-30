import unittest

from .. import manage


class TestImageMessage(unittest.TestCase):
    def test_dump_and_load(self):
        img = manage.ImageMessage(1, 1, 0, 0, manage.IMAGE)
        dumped = img.dump()
        manage.ImageMessage.load(dumped)


class TestUtils(unittest.TestCase):
    def test_dims_to_boxes(self):
        samples = {
            ((100, 100), 1, 1): [(0, 0, 99, 99)],
        }

        for k, v in samples.items():
            self.assertEqual(list(manage.dims_to_boxes(*k)), v)
