from __future__ import annotations

from collections import deque
from typing import List, Any, Callable


class BinaryNode(object):
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left_children = left
        self.right_children = right

    def add_child(self, value) -> BinaryNode:
        """ Add a child Node
        :param value: value of child node
        :return: the current node
        """
        child = BinaryNode(value)
        self.__add_child(child)
        return self

    def travel_bfs(self, reverse: bool = False, zigzag: bool = False, zigzag_reverse: bool = False) -> List[List[Any]]:
        """ Travel the tree in BFS order

        :param reverse: flat to indicate to show output in reverse order
        :param zigzag: flat to indicate to show output in zigzag format [left -> right -> left]
        :param zigzag_reverse: flat to indicate to show output in zigzag format in reverse [right -> left -> right]
        this has priority over zigzag flag
        :return: Array representing each level, and each level Array consists of all values in that level
        """
        output = []

        def zigzag_reverse_identifier() -> Callable[[int], bool]:
            if zigzag_reverse:
                return lambda level: level % 2 != 0
            else:
                return lambda level: level % 2 == 0

        zigzag_reverse_identifier_function: Callable[[int], bool] = zigzag_reverse_identifier()

        def __travel_each_level(queue: deque, level: int = 0):
            if len(queue) == 0:
                return
            next_level = deque()
            level_output = []

            while len(queue) != 0:
                node = queue.popleft()
                if zigzag or zigzag_reverse:
                    if zigzag_reverse_identifier_function(level):
                        level_output.append(node.value)
                    else:
                        level_output.insert(0, node.value)
                else:
                    level_output.append(node.value)

                if node.left_children:
                    next_level.append(node.left_children)
                if node.right_children:
                    next_level.append(node.right_children)

            if reverse:
                output.insert(0, level_output)
            else:
                output.append(level_output)

            __travel_each_level(next_level, level + 1)

        __travel_each_level(deque([self]))
        return output

    def __add_child(self, child) -> None:
        if child.value < self.value:
            if self.left_children:
                self.left_children.__add_child(child)
            else:
                self.left_children = child
        elif child.value > self.value:
            if self.right_children:
                self.right_children.__add_child(child)
            else:
                self.right_children = child
        else:
            print("Value already exists {}".format(child.value))

    def __str__(self, level=0) -> str:
        ret = self.right_children.__str__(level + 1) if self.right_children else ""
        ret += "\t" * level + repr(self.value) + "\n"
        ret += self.left_children.__str__(level + 1) if self.left_children else ""
        return ret
