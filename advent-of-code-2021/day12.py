with open('input/day12.txt') as file:
    input_seq = [line.strip().split('-') for line in file]


class Cave:
    def __init__(self, value):
        self.value = value
        self.connections = []

    def add_connection(self, another):
        self.connections.append(another)

    def __str__(self):
        return self.value


def construct_graph():
    element_map = {}

    def add_into_map(element):
        try:
            _ = element_map[element]
        except KeyError:
            element_map[element] = Cave(element)

    for each in input_seq:
        add_into_map(each[0])
        add_into_map(each[1])

    def make_link(element1, element2):
        cave1 = element_map[element1]
        cave2 = element_map[element2]
        cave1.add_connection(cave2)
        cave2.add_connection(cave1)

    for each in input_seq:
        make_link(each[0], each[1])

    return element_map['start'], element_map['end']


#     start
#     /   \
# c--A-----b--d
#     \   /
#      end

def iterate():
    start, end = construct_graph()

    def can_visit(value, path):
        if value in path:
            return value.isupper()
        else:
            return True

    def find_path(_current, path: list, small_visited=False):
        value = str(_current)
        if not can_visit(value, path):
            if small_visited or value in ['start', 'end']:
                return 0
            small_visited = True
        path.append(value)
        if _current == end:
            print(path)
            return 1
        connection = _current.connections
        count = 0
        for each in connection:
            count += find_path(each, path[:], small_visited)
        return count

    print(find_path(start, []))


if __name__ == '__main__':
    iterate()
