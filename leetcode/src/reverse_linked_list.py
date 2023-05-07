# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        return f'{self.val} -> {str(self.next)}'


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        while current:
            next_node = current.next
            current.next = previous
            previous, current = current, next_node

        return previous
