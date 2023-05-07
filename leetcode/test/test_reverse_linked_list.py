from unittest import TestCase

from leetcode.src.reverse_linked_list import ListNode, Solution


class TestListNode(TestCase):
    def test1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

        reversed_head = Solution().reverseList(head)

        self.assertEqual('5 -> 4 -> 3 -> 2 -> 1 -> None', str(reversed_head))

    def test2(self):
        head = None

        reversed_head = Solution().reverseList(head)

        self.assertEqual('None', str(reversed_head))

    def test3(self):
        head = ListNode(2)

        reversed_head = Solution().reverseList(head)

        self.assertEqual('2 -> None', str(reversed_head))