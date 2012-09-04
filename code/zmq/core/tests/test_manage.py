import unittest

from .. import manage


class TestImageMessage(unittest.TestCase):
    def test_dump_and_load(self):
        img = manage.ImageMessage(1, 1, 0, 0, manage.IMAGE)
        dumped = img.dump()
        manage.ImageMessage.load(dumped)


class TestUtils(unittest.TestCase):
    def test_xgen_coord(self):
        coords = [(0, 0), (0, 1), (1, 0), (1, 1)]
        res = manage.dims_to_coord(2, 2, (2, 2))
        self.assertEqual(list(res), coords)

    def test_coord_boxes(self):
        coords = [[(0, 0), (0, 1)], [(1, 0), (1, 1)]]
        bxs = manage.coords_to_boxes(coords)
        self.assertEqual(list(bxs), [])

    def test_to_rows(self):
        size = 10
        rows = 4
        res = [0, 2, 4, 6, 9]
        self.assertEqual(manage.size_to_rows_cols(size, rows), res)

    def test_boxes_lines(self):
        lines = [0, 2, 4, 6]
        found = manage.make_boxes_two_lines(lines, lines)
        res = [(0, 2), (2, 4), (4, 6)]
        self.assertEqual(found, res)
