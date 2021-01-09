from common_code import BinaryNode


def tree_traversal():
    root: BinaryNode = BinaryNode(1)
    root.left_children = BinaryNode(7).add_left_child(4).add_right_child(5)
    root.right_children = BinaryNode(9).add_left_child(2).add_right_child(7)
    print(root)
    return root.find_all_path(12)


if __name__ == '__main__':
    print(tree_traversal())
