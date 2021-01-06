from __future__ import annotations

from collections import deque
from typing import List, Any


class BinaryNode(object):

    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left_children = left
        self.right_children = right

    def add_child(self, value) -> BinaryNode:
        child = BinaryNode(value)
        self.__add_child(child)
        return self

    def travel_bfs(self) -> List[List[Any]]:
        output = []
        level_output = []
        level_index = 0

        queue = deque()
        queue.append((0, self))
        while len(queue) != 0:
            index, node = queue.popleft()
            if level_index != index:
                level_index = index
                output.append(level_output)
                level_output = []
            level_output.append(node.value)

            if node.left_children:
                queue.append((index + 1, node.left_children))
            if node.right_children:
                queue.append((index + 1, node.right_children))

        output.append(level_output)

        return output

    def travel_bfs_reverse(self) -> List[List[Any]]:
        output = []
        queue = deque()

        def __travel_each_level(level_idx, first_element: BinaryNode):
            level_output = [first_element.value]

            while True:
                if first_element.left_children:
                    queue.append((level_idx + 1, first_element.left_children))
                if first_element.right_children:
                    queue.append((level_idx + 1, first_element.right_children))

                if len(queue) == 0:
                    break
                index, node = queue.popleft()

                if index != level_idx:
                    __travel_each_level(index, node)
                    break
                else:
                    level_output.append(node.value)
                    first_element = node

            output.append(level_output)

        __travel_each_level(0, self)
        return output

    def travel_bfs_zigzag(self) -> List[List[Any]]:
        output = []

        def __travel_each_level(stack: list, level: int = 0):
            if len(stack) == 0:
                return
            next_level = []
            level_output = []
            while len(stack) != 0:
                node = stack.pop()
                level_output.append(node.value)

                if level % 2 == 0:
                    if node.left_children:
                        next_level.append(node.left_children)
                    if node.right_children:
                        next_level.append(node.right_children)
                else:
                    if node.right_children:
                        next_level.append(node.right_children)
                    if node.left_children:
                        next_level.append(node.left_children)

            output.append(level_output)
            __travel_each_level(next_level, level + 1)

        __travel_each_level([self])
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
