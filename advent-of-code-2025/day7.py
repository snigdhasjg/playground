import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.INFO
DAY = 7
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = True


class Location:
    def __init__(self, value):
        self.value = value
        self.path = 1 if value == 'S' else 0

    def make_path(self, above: 'Location'):
        self.path += above.path

    def should_ignore(self) -> bool:
        return self.path == 0

    def should_split(self) -> bool:
        return self.value == '^'

    def __repr__(self):
        return '|' if self.path != 0 else self.value


def part1_example():
    return """\
        .......S.......
        ...............
        .......^.......
        ...............
        ......^.^......
        ...............
        .....^.^.^.....
        ...............
        ....^.^...^....
        ...............
        ...^.^...^.^...
        ...............
        ..^...^.....^..
        ...............
        .^.^.^.^.^...^.
        ..............."""


def part1(raw_input: str):
    parsed_input = list(map(lambda a: list(map(lambda b: Location(b), list(a))), raw_input.splitlines()))

    max_y = len(parsed_input)
    max_x = len(parsed_input[0])
    count_split = 0

    for y in range(max_y):
        for x in range(max_x):
            position_value = parsed_input[y][x]
            if position_value.should_ignore():
                continue

            if y + 1 >= max_y:
                break
            next_row_value = parsed_input[y + 1][x]
            if next_row_value.should_split():
                count_split += 1
                parsed_input[y + 1][x - 1].make_path(position_value)
                parsed_input[y + 1][x + 1].make_path(position_value)
            else:
                next_row_value.make_path(position_value)
        LOG.debug(''.join(map(str, parsed_input[y])))

    return count_split


def part2_example():
    return """\
        .......S.......
        ...............
        .......^.......
        ...............
        ......^.^......
        ...............
        .....^.^.^.....
        ...............
        ....^.^...^....
        ...............
        ...^.^...^.^...
        ...............
        ..^...^.....^..
        ...............
        .^.^.^.^.^...^.
        ..............."""


def part2(raw_input: str):
    parsed_input = list(map(lambda a: list(map(lambda b: Location(b), list(a))), raw_input.splitlines()))

    max_y = len(parsed_input)
    max_x = len(parsed_input[0])

    for y in range(max_y):
        for x in range(max_x):
            position_value = parsed_input[y][x]
            if position_value.should_ignore():
                continue

            if y + 1 >= max_y:
                break
            next_row_value = parsed_input[y + 1][x]
            if next_row_value.should_split():
                parsed_input[y + 1][x - 1].make_path(position_value)
                parsed_input[y + 1][x + 1].make_path(position_value)
            else:
                next_row_value.make_path(position_value)
        LOG.debug(''.join(map(str, parsed_input[y])))

    return sum(map(lambda c: c.path, parsed_input[-1]))
