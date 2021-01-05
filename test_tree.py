from unittest import TestCase
from tree import Node


class TestNode(TestCase):

    def test_str_method_should_print_tree_in_proper_format(self):
        node11 = Node(1)
        node12 = Node(3)
        node1 = Node(2, node11, node12)
        node21 = Node(5)
        node22 = Node(7)
        node2 = Node(6, node21, node22)
        head = Node(4, node1, node2)

        expected = "\t\t1\n\t2\n\t\t3\n4\n\t\t5\n\t6\n\t\t7\n"

        self.assertEqual(str(head), expected)

    def test_should_add_nodes(self):
        head = Node(4)
        head.add_child(2).add_child(1).add_child(3).add_child(6).add_child(5).add_child(7)

        expected = "\t\t1\n\t2\n\t\t3\n4\n\t\t5\n\t6\n\t\t7\n"

        self.assertEqual(str(head), expected)

