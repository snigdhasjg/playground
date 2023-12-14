import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG
DAY = 14
DEVELOPMENT_PHASE = True
PART_1_ENABLE = False
PART_2_ENABLE = True


def part1_example():
    return """\
        O....#....
        O.OO#....#
        .....##...
        OO.#O....O
        .O.....O#.
        O.#..O.#.#
        ..O..#O..O
        .......O..
        #....###..
        #OO..#...."""


class Group:
    def __init__(self, rocks: str, starting_pos):
        self.rocks = rocks
        self.rounded_rocks_count = rocks.count('O')
        self.starting_pos = starting_pos

    def load(self):
        return sum(map(lambda x: self.starting_pos - x, range(self.rounded_rocks_count)))

    def __repr__(self):
        return f'{self.starting_pos}: {self.rocks}({self.rounded_rocks_count})'


class Line:
    def __init__(self, rocks: str):
        self.groups = []
        visited_length = len(rocks)
        for idx, group in enumerate(rocks.split('#')):
            if 'O' in group:
                self.groups.append(Group(group, visited_length))
            visited_length = visited_length - 1 - len(group)

        LOG.debug(self)

    def load(self):
        return sum(map(lambda x: x.load(), self.groups))

    def __repr__(self):
        return f'[\n\t{"\n\t".join(map(repr, self.groups))} \n] -> {self.load()}'


def part1(raw_input: str):
    raw_input_lines = raw_input.splitlines()
    lines = [''] * len(raw_input_lines[0])
    for each_row in raw_input_lines:
        for idx, each_char in enumerate(each_row):
            lines[idx] += each_char

    return sum([Line(rocks).load() for rocks in lines])


def part2_example():
    return """\
        O....#....
        O.OO#....#
        .....##...
        OO.#O....O
        .O.....O#.
        O.#..O.#.#
        ..O..#O..O
        .......O..
        #....###..
        #OO..#...."""


def part2(raw_input: str):
    pass
