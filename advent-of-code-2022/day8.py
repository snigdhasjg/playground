def parse_input():
    with open('input/day8.txt') as file:
        return [list(map(lambda x: int(x), list(line.strip()))) for line in file]


def part1():
    grid_of_trees = parse_input()
    height, width = len(grid_of_trees), len(grid_of_trees[0])

    def check_tree_is_visible(x, y):
        if x == 0 or y == 0 or x == height - 1 or y == width - 1:
            return True
        node_value = grid_of_trees[x][y]

        def visibility_check(start, stop, step, is_x_axis=True):
            for new_pos in range(start, stop, step):
                current_node = grid_of_trees[new_pos][y] if is_x_axis else grid_of_trees[x][new_pos]
                if node_value <= current_node:
                    return False
            return True

        if visibility_check(x - 1, -1, -1):
            return True
        if visibility_check(x + 1, height, 1):
            return True
        if visibility_check(y - 1, -1, -1, False):
            return True
        if visibility_check(y + 1, width, 1, False):
            return True

        return False

    count = 0
    for i in range(height):
        for j in range(width):
            if check_tree_is_visible(i, j):
                count += 1
            #     print('T', end='')
            # else:
            #     print(' ', end='')
        # print()

    print(count)


def part2():
    grid_of_trees = parse_input()
    height, width = len(grid_of_trees), len(grid_of_trees[0])

    def visibility_score(x, y):
        if x == 0 or y == 0 or x == height - 1 or y == width - 1:
            return 0
        node_value = grid_of_trees[x][y]

        def visible_tree(start, stop, step, is_x_axis=True):
            visibility_count = 0
            for new_pos in range(start, stop, step):
                current_node = grid_of_trees[new_pos][y] if is_x_axis else grid_of_trees[x][new_pos]
                visibility_count += 1
                if node_value <= current_node:
                    return visibility_count
            return visibility_count

        return visible_tree(x - 1, -1, -1) * visible_tree(x + 1, height, 1) \
               * visible_tree(y - 1, -1, -1, False) * visible_tree(y + 1, width, 1, False)

    highest_score = 0
    for i in range(height):
        for j in range(width):
            highest_score = max(highest_score, visibility_score(i, j))
            #     print('T', end='')
            # else:
            #     print(' ', end='')
        # print()

    print(highest_score)


if __name__ == '__main__':
    part2()
