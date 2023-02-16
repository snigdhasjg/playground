import math
import sys

sys.setrecursionlimit(10000)


def parse_input():
    with open('input/day12.txt') as file:
        height_grid = [list(line.strip()) for line in file]

    start = None
    end = None
    for i in range(len(height_grid)):
        for j in range(len(height_grid[0])):
            if height_grid[i][j] == 'S':
                start = (i, j)
                height_grid[i][j] = 'a'
            if height_grid[i][j] == 'E':
                end = (i, j)
                height_grid[i][j] = 'z'
            height_grid[i][j] = ord(height_grid[i][j]) - ord('a')

    print('\n'.join([' '.join(map(lambda x: '\t{}'.format(x), each)) for each in height_grid]))
    print('start: {}, end: {}'.format(start, end))
    return height_grid, start, end


def process():
    height_grid, start, end = parse_input()
    grid_len_x = len(height_grid)
    grid_len_y = len(height_grid[0])
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    memory_map = {}

    def climb(x, y, visited_map):
        if x == end[0] and y == end[1]:
            return 0
        if (x, y) in visited_map:
            return math.inf
        visited_map[(x, y)] = True
        if (x, y) in memory_map:
            return memory_map[(x, y)]

        current_height = height_grid[x][y]
        step_count = math.inf
        for direction in directions:
            new_direction = (x + direction[0], y + direction[1])
            if 0 <= new_direction[0] < grid_len_x and 0 <= new_direction[1] < grid_len_y \
                    and height_grid[new_direction[0]][new_direction[1]] - current_height <= 1:
                step_count = min(step_count, climb(new_direction[0], new_direction[1], visited_map.copy()))

        if step_count == math.inf:
            print('no path found from ({},{})'.format(x, y))
            memory_map[(x, y)] = math.inf
            return math.inf

        memory_map[(x, y)] = 1 + step_count
        print('({},{}) -> {}'.format(x, y, 1 + step_count))
        return 1 + step_count

    print(climb(start[0], start[1], {}))


if __name__ == '__main__':
    process()
