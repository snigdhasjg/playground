import logging
import math

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG
DAY = 10
DEVELOPMENT_PHASE = False
PART_1_ENABLE = False
PART_2_ENABLE = True

CHAR_MAPPING = {
    'F': '\u250C',
    '|': '\u2502',
    '-': '\u2500',
    '7': '\u2510',
    'L': '\u2514',
    'J': '\u2518',
    '.': '.',
    'S': 'S'
}


class Tile:
    distance: int = math.inf

    def __init__(self, index: tuple[int, int], value: str):
        self.index: tuple[int, int] = index
        self.value: str = value

    def is_starting(self):
        return self.value == 'S'

    def update_distance(self, distance):
        if distance < self.distance:
            self.distance = distance
            return True
        return False

    def is_valid_neighbouring_tile(self, another_tile: 'Tile'):
        delta_y = self.index[0] - another_tile.index[0]  # +1 meaning up and -1 meaning down
        delta_x = self.index[1] - another_tile.index[1]  # +1 meaning left and -1 meaning right

        allowed_based_on_position = False

        if delta_y == -1:
            allowed_based_on_position = another_tile.value in ('J', '|', 'L')
        elif delta_y == 1:
            allowed_based_on_position = another_tile.value in ('F', '|', '7')
        elif delta_x == -1:
            allowed_based_on_position = another_tile.value in ('J', '-', '7')
        elif delta_x == 1:
            allowed_based_on_position = another_tile.value in ('F', '-', 'L')

        return allowed_based_on_position

    def all_possible_neighbour_tile_indexes(self):
        y = self.index[0]
        x = self.index[1]

        if self.value == 'S':
            return [
                (y + 1, x),
                (y - 1, x),
                (y, x + 1),
                (y, x - 1)
            ]
        if self.value == 'F':
            return [
                (y + 1, x),
                (y, x + 1)
            ]
        if self.value == 'L':
            return [
                (y - 1, x),
                (y, x + 1)
            ]
        if self.value == '7':
            return [
                (y + 1, x),
                (y, x - 1)
            ]
        if self.value == 'J':
            return [
                (y - 1, x),
                (y, x - 1)
            ]
        if self.value == '-':
            return [
                (y, x + 1),
                (y, x - 1)
            ]
        if self.value == '|':
            return [
                (y + 1, x),
                (y - 1, x)
            ]

        return []

    def __str__(self):
        return f'{self.value} ({self.distance})'

    def __repr__(self):
        return str(self)


def part1_example():
    return """\
        -L|F7
        7S-7|
        L|7||
        -L-J|
        L|-JF"""


def part1(raw_input: str):
    pipes = process(raw_input)

    max_distance = -1
    for _, value in pipes.items():
        if value.distance is not math.inf:
            max_distance = max(max_distance, value.distance)

    return max_distance


def process(raw_input):
    LOG.debug('\n'.join([
        ''.join(map(lambda x: CHAR_MAPPING[x], list(each_line)))
        for each_line in raw_input.splitlines()
    ]))

    stack: list[Tile] = []
    pipes: dict[tuple[int, int], Tile] = {}

    for idx_y, each_line in enumerate(raw_input.splitlines()):
        for idx_x, each_char in enumerate(list(each_line)):
            tile = Tile((idx_y, idx_x), each_char)
            pipes[tile.index] = tile

            if tile.is_starting():
                tile.update_distance(0)
                stack.append(tile)

    while len(stack) != 0:
        current_tile = stack.pop()

        for each_tile_indexes in current_tile.all_possible_neighbour_tile_indexes():
            if each_tile_indexes in pipes:
                another_tile = pipes[each_tile_indexes]
                if current_tile.is_valid_neighbouring_tile(another_tile):
                    have_updated = another_tile.update_distance(current_tile.distance + 1)
                    if have_updated:
                        stack.append(another_tile)

    return pipes


def part2_example():
    return """\
        ...........
        .S-------7.
        .|F-----7|.
        .||.....||.
        .||.....||.
        .|L-7.F-J|.
        .|..|.|..|.
        .L--J.L--J.
        ..........."""


def part2(raw_input: str):
    stack: list[Tile] = []
    pipes: dict[tuple[int, int], Tile] = {}

    for idx_y, each_line in enumerate(raw_input.splitlines()):
        for idx_x, each_char in enumerate(list(each_line)):
            tile = Tile((idx_y, idx_x), each_char)
            pipes[tile.index] = tile

            if tile.is_starting():
                tile.update_distance(0)
                stack.append(tile)

    previous_tile = None
    while len(stack) != 0:
        current_tile = stack.pop()

        already_visited_one = False
        for each_tile_indexes in current_tile.all_possible_neighbour_tile_indexes():
            if each_tile_indexes in pipes:
                another_tile = pipes[each_tile_indexes]
                if current_tile.is_valid_neighbouring_tile(another_tile):
                    if (previous_tile and previous_tile == another_tile) or already_visited_one:
                        continue
                    already_visited_one = True
                    have_updated = another_tile.update_distance(current_tile.distance + 1)
                    if have_updated:
                        stack.append(another_tile)

        previous_tile = current_tile

    loop = sorted([v for k, v in pipes.items() if v.distance is not math.inf], key=lambda x: x.distance)

    def determinant(index_a, index_b):
        return index_a[1] * index_b[0] - index_b[1] * index_a[0]

    # https://en.wikipedia.org/wiki/Shoelace_formula
    two_time_area = determinant(loop[-1].index, loop[0].index)
    for i in range(len(loop) - 1):
        two_time_area += determinant(loop[i].index, loop[i + 1].index)
    area = two_time_area // 2

    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    total_boundary_points = len(loop)
    return abs(area) + 1 - total_boundary_points // 2


