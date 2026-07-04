import unittest
import os
from core.utils import get_readable_file_size

class TestUtils(unittest.TestCase):
    def test_readable_file_size_nonexistent(self):
        self.assertEqual(get_readable_file_size("non_existent_file_path_xyz.txt"), "0 Bytes")