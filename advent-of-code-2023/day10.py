import logging
import math

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG
DAY = 10
DEVELOPMENT_PHASE = True
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

    def is_corner(self):
        return self.value in ['F', 'L', 'J', '7']

    def is_horizontal_line(self):
        return self.value == '-'

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
        .F----7F7F7F7F-7....
        .|F--7||||||||FJ....
        .||.FJ||||||||L7....
        FJL7L7LJLJ||LJ.L-7..
        L--J.L7...LJS7F-7L7.
        ....F-J..F7FJ|L7L7L7
        ....L7.F7||L7|.L7L7|
        .....|FJLJ|FJ|F7|.LJ
        ....FJL-7.||.||||...
        ....L---J.LJ.LJLJ..."""


def part2(raw_input: str):
    pipes = process(raw_input)

    max_y = len(raw_input.splitlines())
    max_x = len(raw_input.splitlines()[0])

    loop = {}
    non_loop = []
    for k, v in pipes.items():
        if v.distance is not math.inf:
            loop[k] = v
        else:
            non_loop.append(v)

    count_inside_loop = 0

    # https://en.wikipedia.org/wiki/Point_in_polygon
    for tile in non_loop:
        count_ray_intersection_incrementally = 0
        ray_y, ray_x = tile.index[0] + 1, tile.index[1] + 1
        while ray_y < max_y and ray_x < max_x:
            if (ray_y, ray_x) in loop:
                count_ray_intersection_incrementally += 1
            ray_y += 1
            ray_x += 1

        count_ray_intersection_detrimentally = 0
        ray_y, ray_x = tile.index[0] - 1, tile.index[1] - 1
        while ray_y >= 0 and ray_x >= 0:
            if (ray_y, ray_x) in loop:
                count_ray_intersection_detrimentally += 1
            ray_y -= 1
            ray_x -= 1

        if count_ray_intersection_incrementally % 2 == 1 and count_ray_intersection_detrimentally % 2 == 1:
            count_inside_loop += 1

    return count_inside_loop
