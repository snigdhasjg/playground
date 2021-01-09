from __future__ import annotations

from typing import Callable, Any, Tuple

from multipledispatch import dispatch


class LinkedListException(Exception):
    pass


class Node(object):
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.__nextNode: Node = None

    @dispatch()
    def next_node(self) -> Node:
        return self.__nextNode

    @dispatch(object)
    def next_node(self, next_node: Node) -> None:
        self.__nextNode = next_node

    def __str__(self) -> str:
        return "Node({})".format(self.data)


class LinkedList:
    def __init__(self, init_value: list = None) -> None:
        """ A linked list is a linear collection of data elements whose order is not given by their physical placement
         in memory. Instead, each element points to the next. It is a data structure consisting of a collection of
          nodes which together represent a sequence.
        :param init_value: If you want to initiate linked list with help of other list
        """
        self.__head: Node = None
        self.__size: int = 0
        if init_value:
            for each in init_value:
                self.add_element(each)

    def add_element(self, value: Any) -> None:
        """ Add element to linked list at the end
        :param value: value of the node
        :raises LinkedListException: If cycle exists
        """
        if self.is_cycle_exists():
            raise LinkedListException("Cycle exists")
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            temp: Node = self.__head
            while temp.next_node():
                temp = temp.next_node()
            temp.next_node(new_node)
        self.__size += 1

    def add_cycle(self, index) -> None:
        """ To add a cycle in the linked list at given index.
        This method will connect tail of linked list with given index.
        :param index: Where to start the cycle
        :raises LinkedListException: If cycle already exists OR input index exceeds the length of list
        """
        if self.is_cycle_exists():
            raise LinkedListException("Cycle already exists")
        if self.__size < index:
            raise LinkedListException("Index must bve less than or equals to " + str(self.__size))
        start_idx = 0
        cycle_start_node: Node = self.__head
        while start_idx < index:
            cycle_start_node = cycle_start_node.next_node()
            start_idx += 1

        temp = self.__head
        for _ in range(self.__size - 1):
            temp = temp.next_node()
        temp.next_node(cycle_start_node)

    def is_cycle_exists(self) -> bool:
        """ To find out whether a cycle exits in the linked list or not
        :return: bool
        """
        slow: Node = self.__head
        fast: Node = slow
        cycle_exists = False
        while slow is not None and fast is not None:
            slow = slow.next_node()
            fast_next_node = fast.next_node()
            if fast_next_node is None:
                break
            fast = fast_next_node.next_node()
            if slow == fast:
                cycle_exists = True
                break

        return cycle_exists

    def get_head(self) -> Node:
        """ Get head node of the linked list
        :return: Node
        """
        return self.__head

    def reverse(self, current: Node = None, prev: Node = None) -> None:
        """ Reverse a liked list,
        it also updates the head of the linked list after reversing the linked list
        :param current: current node of the linked list while traversing
        :param prev: previous node of the current code
        """
        if current is None and prev is None:
            current = self.__head
        elif current is None:
            self.__head = prev
            return
        self.reverse(current.next_node(), current)
        current.next_node(prev)

    def reverse_set_of_list(self, p: int, q: int) -> None:
        """ reverse a set within a linked list
        it also updates the head (if required) of the linked list
        :param p: start position
        :param q: end position
        :raises LinkedListException if value of p less than 1 and q greater than size
        """
        if p <= 0:
            raise LinkedListException("Limit must be greater than or equals to 1")

        def raise_exception_if_next_node_null(node: Node) -> bool:
            if node.next_node() is None:
                raise LinkedListException(f"Limit must be less than or equals to {self.__size}")
            return True

        temp: Node = self.__head
        idx = 1
        while idx != p:
            start = temp
            temp = temp.next_node()
            idx += 1
            self.__swap_set(start, temp, None, q - p, raise_exception_if_next_node_null)

    def reverse_set_of_list_with_size(self, k: int) -> None:
        """ Reverse every set of K element from start to end
        if K exceeds end of the list, then reverse that
        :param k: element to reverse
        """
        temp: Node = self.__head
        start: Node = None
        while temp is not None:
            start, temp = temp, self.__swap_set(start, temp, None, k - 1)

    def rotate(self, k: int) -> None:
        self.__rotate(k, None, self.__head)

    def __rotate(self, k: int, prev: Node, current: Node, depth: int = 1) -> Tuple[int, int, Node]:
        if current is None:
            return 1, depth - 1, None
        reverse_depth, size, last_node = self.__rotate(k, current, current.next_node(), depth + 1)
        if last_node is None:
            last_node = current
        if reverse_depth == k % size:
            prev.next_node(None)
            last_node.next_node(self.__head)
            self.__head = current
        return reverse_depth + 1, size, last_node

    def __swap_set(self, start: Node, current: Node, prev: Node, no_of_element: int,
                   is_end_of_list: Callable[[Node], bool] = lambda node: node.next_node() is None) -> Node:
        if is_end_of_list(current) or no_of_element == 0:
            _temp = current.next_node()
            if start is None:
                self.__head = current
            else:
                start.next_node(current)
            current.next_node(prev)
            return _temp
        end = self.__swap_set(start, current.next_node(), current, no_of_element - 1, is_end_of_list)
        if prev is None:
            current.next_node(end)
        else:
            current.next_node(prev)
        return end

    def __sizeof__(self) -> int:
        return self.__size

    def __str__(self) -> str:
        temp = self.__head
        str_list = ""
        for _ in range(self.__size):
            str_list += str(temp) + "->"
            temp = temp.next_node()
        return str_list + str(temp)
