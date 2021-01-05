with open('input/day3.txt') as file:
    tree_map = []
    for each_line in file:
        tree_map.append(list(each_line.strip()))

size_x = len(tree_map[0])
size_y = len(tree_map)

tree_found = 0


def get_next_coordinate(dx, dy, x=0, y=0):
    if y >= size_y:
        return
    if tree_map[y][x] == '#':
        global tree_found
        tree_found += 1
    new_x = (x + dx) % size_x
    get_next_coordinate(dx, dy, new_x, y + dy)


if __name__ == '__main__':
    # get_next_coordinate(1, 1)  # 104
    # get_next_coordinate(3, 1)  # 230
    # get_next_coordinate(5, 1)  # 83
    # get_next_coordinate(7, 1)  # 98
    # get_next_coordinate(1, 2)  # 49
    print(tree_found)
