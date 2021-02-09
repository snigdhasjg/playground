def process_input():
    edges = [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]
    unique_node = set()
    dependencies = {}
    childrens = {}
    for pair in edges:
        unique_node.add(pair[0])
        unique_node.add(pair[1])

        dependency: list = dependencies.get(pair[1])
        if dependency:
            dependency.append(pair[0])
        else:
            dependencies[pair[1]] = [pair[0]]

        child: list = childrens.get(pair[0])
        if child:
            child.append(pair[1])
        else:
            childrens[pair[0]] = [pair[1]]

    return unique_node, dependencies, childrens


def solve():
    unique_node, dependencies, childrens = process_input()
    output = []
    for value in unique_node:
        dependency = dependencies.get(value)
        if not dependency:
            output.append(value)
            unique_node.remove(value)
            break

    for _ in range(len(unique_node)):
        last_element = output[-1]
        childrens.
