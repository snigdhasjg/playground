# https://leetcode.com/problems/kth-largest-element-in-a-stream/
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k - 1
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        inserted = False
        for i in range(len(self.nums)):
            current = self.nums[i]
            if current > val:
                continue
            if current <= val:
                self.nums.insert(i, val)
                inserted = True
                break

        if not inserted:
            self.nums.append(val)

        return self.nums[self.k]

    def __str__(self):
        def value(idx):
            val = self.nums[idx]
            if idx == self.k:
                return f'[{val}]'
            return str(val)

        return ' -> '.join([value(i) for i in range(len(self.nums))])

10110011