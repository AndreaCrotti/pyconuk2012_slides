import unittest

from .. import manage


class TestImageMessage(unittest.TestCase):
    def test_dump_and_load(self):
        img = manage.ImageMessage(1, 1, 0, 0, manage.IMAGE)
        dumped = img.dump()
        manage.ImageMessage.load(dumped)
