import itertools
import math


class Node:
    def __init__(self, value, dummy_node=False):
        self.value = value
        self.dummy_node = dummy_node
        # Parent for Tree
        self.parent: Node = None
        # Child for Tree
        self.left_child: Node = None
        self.right_child: Node = None
        # Link for DoublyLinkedList
        self.left_link: Node = None
        self.right_link: Node = None

    def magnitude(self):
        if self.dummy_node:
            return 3 * self.left_child.magnitude() + 2 * self.right_child.magnitude()
        return self.value

    def explode(self, depth=1) -> bool:
        if depth == 5 and self.dummy_node:
            # print('Explode at level 5', str(self))
            self.__explode()
            return True
        if self.left_child:
            left_child_result = self.left_child.explode(depth + 1)
            if left_child_result:
                return True
        if self.right_child:
            right_child_result = self.right_child.explode(depth + 1)
            if right_child_result:
                return True
        return False

    def split(self):
        if not self.dummy_node and self.value >= 10:
            # print('Split', str(self))
            self.__split()
            return True
        if self.left_child:
            left_child_result = self.left_child.split()
            if left_child_result:
                return True
        if self.right_child:
            right_child_result = self.right_child.split()
            if right_child_result:
                return True
        return False

    def __split(self):
        if self.dummy_node:
            raise "Split not possible on dummy node"
        split_value = self.value / 2
        self.value = '(O)'
        self.dummy_node = True

        # Setting new node and its link & parent
        left_node: Node = Node(math.floor(split_value))
        right_node: Node = Node(math.ceil(split_value))
        left_node.right_link = right_node
        right_node.left_link = left_node
        left_node.parent = self
        right_node.parent = self
        self.left_child = left_node
        self.right_child = right_node

        # fixing link
        if self.left_link:
            left_node.left_link = self.left_link
            self.left_link.right_link = left_node
        if self.right_link:
            right_node.right_link = self.right_link
            self.right_link.left_link = right_node

        self.left_link = None
        self.right_link = None

    def __explode(self):
        if not self.dummy_node:
            raise "Explode not possible on value node"
        self.value = 0
        self.dummy_node = False

        left_child: Node = self.left_child
        right_child: Node = self.right_child
        self.left_link: Node = left_child.left_link
        self.right_link: Node = right_child.right_link
        self.left_child = None
        self.right_child = None

        if self.left_link:
            self.left_link.value += left_child.value
            self.left_link.right_link = self
        if self.right_link:
            self.right_link.value += right_child.value
            self.right_link.left_link = self

    def __str__(self):
        if self.dummy_node:
            return '[' + str(self.left_child) + ',' + str(self.right_child) + ']'
        return str(self.value)

    def str_linked_list(self):
        return self.left_most_link().__str_linked_list()

    def __str_linked_list(self):
        out = str(self.value)
        if self.right_link:
            out += ' -> ' + self.right_link.__str_linked_list()
        return out

    def left_most_link(self):
        if not self.left_child:
            return self
        return self.left_child.left_most_link()

    def right_most_link(self):
        if not self.right_child:
            return self
        return self.right_child.right_most_link()

    def __add__(self, other):
        parent_node: Node = create_parent_node(self, other)
        right_link_of_left_node: Node = self.right_most_link()
        left_link_of_right_node: Node = other.left_most_link()

        right_link_of_left_node.right_link = left_link_of_right_node
        left_link_of_right_node.left_link = right_link_of_left_node

        while parent_node.explode() or parent_node.split():
            # print(top_most_node)
            # print(top_most_node.str_linked_list())
            pass

        return parent_node


def create_parent_node(first_element: Node, second_element: Node):
    new_element: Node = Node('(X)', dummy_node=True)
    # setting child
    new_element.left_child = first_element
    new_element.right_child = second_element
    # setting parent
    second_element.parent = new_element
    first_element.parent = new_element
    return new_element


def process_each_line(_line):  # [[[[4,3],4],4],[7,[[8,4],9]]]
    stack = []
    end_link: Node = None
    for each in list(_line):
        if each in ['[', ',']:
            continue
        elif each == ']':
            second_element: Node = stack.pop()
            first_element: Node = stack.pop()
            new_element: Node = create_parent_node(first_element, second_element)

            stack.append(new_element)
        else:
            new_node = Node(int(each))
            if end_link:
                end_link.right_link = new_node
                new_node.left_link = end_link
            end_link = new_node
            stack.append(new_node)
    return stack[0]


def process_input_part1():
    with open('input/day18.txt') as file:
        input_numbers = [process_each_line(line.strip()) for line in file]

    return input_numbers


def process_input_part2():
    with open('input/day18.txt') as file:
        input_numbers = [line.strip() for line in file]

    return input_numbers


def add_inputs_part_1():
    inputs = process_input_part1()
    temp_node = inputs[0]
    for each_node in inputs[1:]:
        temp_node += each_node

    return str(temp_node), temp_node.magnitude()


def add_inputs_part_2():
    _input = process_input_part2()
    combination_index = itertools.combinations(range(len(_input)), 2)
    max_mag = -1
    max_node = None

    def add(_x, _y):
        first_node = process_each_line(_input[_x])
        second_node = process_each_line(_input[_y])

        added_node = first_node + second_node
        return added_node, added_node.magnitude()

    for x, y in combination_index:
        fs_node, fs_mag = add(x, y)
        if fs_mag > max_mag:
            # print('max', x, y, fs_mag, str(fs_node))
            max_mag = fs_mag
            max_node = fs_node

        fs_node, fs_mag = add(y, x)
        if fs_mag > max_mag:
            # print('max', x, y, fs_mag, str(fs_node))
            max_mag = fs_mag
            max_node = fs_node

    return str(max_node), max_mag


if __name__ == '__main__':
    print(add_inputs_part_2())
