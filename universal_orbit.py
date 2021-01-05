inputs = []
with open("data/orbit_map.txt") as file:
    for line in file:
        inputs.append(line.strip().split(')'))


class Node:
    def __init__(self, t):
        self.value = t
        self.children = list()

    def add_child(self, new_node):
        self.children.append(new_node)

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret


def insert_into_nodes(node: Node):
    for i in filter(lambda x: x[0] == node.value, inputs):
        node.add_child(Node(i[1]))


def make_tree(node: Node):
    insert_into_nodes(node)
    for each_node in node.children:
        make_tree(each_node)


def calculate_orbits(node: Node, level: int = 0) -> int:
    total = level * 1
    for each_node in node.children:
        total += calculate_orbits(each_node, level + 1)
    return total


def find_you_and_san(node: Node):
    found_on_same_level = False
    found_on_level = list()
    for each_node in node.children:
        if each_node.value in ['YOU', 'SAN']:
            found_on_same_level = True
        is_found, level = find_you_and_san(each_node)
        if level == -1:
            return True, level
        if is_found:
            found_on_level.append(level)
    length_of_array = len(found_on_level)

    if found_on_same_level and length_of_array > 0:
        print(node.value, "Yay found", found_on_level)
        return True, -1
    if length_of_array == 2:
        print(node.value, "Yay found", found_on_level)
        return True, -1
    if length_of_array == 1:
        return True, 1 + found_on_level[0]
    if found_on_same_level:
        return True, 1
    return False, 0


if __name__ == '__main__':
    root = Node('COM')
    make_tree(root)
    print(str(root))
