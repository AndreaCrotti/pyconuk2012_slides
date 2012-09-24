import unittest

from mock import patch

@patch('ext.module.function', new=lambda x: 42)
class TestMyClass(unittest.TestCase):
    def setUp(self):
        pass
    # ...
