from unittest import TestCase

from leetcode.src.kth_largest_element import KthLargest


class TestKthLargest(TestCase):
    def test1(self):
        kth_largest = KthLargest(3, [4, 5, 8, 2])

        self.assertEqual(4, kth_largest.add(3))
        self.assertEqual(5, kth_largest.add(5))
        self.assertEqual(5, kth_largest.add(10))
        self.assertEqual(8, kth_largest.add(9))
        self.assertEqual(8, kth_largest.add(4))

    def test2(self):
        kth_largest = KthLargest(1, [])

        self.assertEqual(-3, kth_largest.add(-3))
        self.assertEqual(-2, kth_largest.add(-2))
        self.assertEqual(-2, kth_largest.add(-4))
        self.assertEqual(0, kth_largest.add(0))
        self.assertEqual(4, kth_largest.add(4))

    def test3(self):
        kth_largest = KthLargest(2, [0])

        self.assertEqual(-1, kth_largest.add(-1))
        self.assertEqual(0, kth_largest.add(1))
        self.assertEqual(0, kth_largest.add(-2))
        self.assertEqual(0, kth_largest.add(-4))
        self.assertEqual(1, kth_largest.add(3))
