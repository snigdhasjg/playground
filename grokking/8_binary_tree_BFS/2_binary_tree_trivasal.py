from common_code import BinaryNode


def tree_traversal():
    root: BinaryNode = BinaryNode(5) \
        .add_child(3).add_child(4).add_child(9).add_child(7).add_child(10).add_child(6).add_child(8)
    print(root)
    return root.travel_bfs(zigzag_reverse=True)


if __name__ == '__main__':
    print(tree_traversal())
