import unittest

from leetcode.src.zigzag_conversion import convert


class Test(unittest.TestCase):
    def test1(self):
        # P   A   H   N
        # A P L S I I G
        # Y   I   R
        self.assertEqual('PAHNAPLSIIGYIR', convert('PAYPALISHIRING', 3))

    def test2(self):
        # P     I    N
        # A   L S  I G
        # Y A   H R
        # P     I
        self.assertEqual('PINALSIGYAHRPI', convert('PAYPALISHIRING', 4))

    def test3(self):
        self.assertEqual('A', convert('A', 1))
