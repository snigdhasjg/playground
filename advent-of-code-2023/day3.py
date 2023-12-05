import logging
from dataclasses import dataclass
from functools import reduce

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.CRITICAL
DAY = 3
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = True


def part1_example():
    return """\
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598.."""


@dataclass
class NumberInfo:
    y_idx: int
    x_end_index: int
    number: int
    length: int

    def __post_init__(self):
        self.x_min = self.x_end_index - self.length
        self.x_max = self.x_end_index - 1

    def __hash__(self):
        return hash((self.y_idx, self.x_end_index, self.number, self.length))

    def __repr__(self):
        return f'Number {self.number} on line {self.y_idx} from {self.x_min} to {self.x_max} index'

    def all_occupied_positions(self):
        return [(self.y_idx, x) for x in range(self.x_min, self.x_max + 1)]

    def is_adjacent(self, symbols: dict[tuple[int, int], str]):
        LOG.debug(self)
        for y in range(self.y_idx - 1, self.y_idx + 2):
            for x in range(self.x_min - 1, self.x_max + 2):
                if y == self.y_idx and self.x_min <= x <= self.x_max:
                    # This condition is to reduce checks on symbols dict
                    continue
                if (y, x) in symbols:
                    LOG.debug(f'\t{self.number} is adjacent to {symbols[(y, x)]} at index({y},{x})')
                    return True
        LOG.debug(f'\t{self.number} is alone')
        return False


def process_parts(raw_input):
    numbers: list[NumberInfo] = []
    symbols = {}

    def parse(_y_idx, line: str):
        buffer = ''

        for x_idx in range(len(line)):
            each_char = line[x_idx]
            if each_char.isdigit():
                buffer += each_char
            else:
                if buffer != '':
                    numbers.append(NumberInfo(y_idx, x_idx, int(buffer), len(buffer)))
                    buffer = ''
                if each_char != '.':
                    symbols[(y_idx, x_idx)] = each_char
        if buffer != '':
            numbers.append(NumberInfo(y_idx, len(line), int(buffer), len(buffer)))

    for y_idx, each_line in enumerate(raw_input.splitlines()):
        parse(y_idx, each_line)
    return numbers, symbols


def part1(raw_input):
    numbers, symbols = process_parts(raw_input)

    sum_of_all_part_numbers = 0
    for each_number in numbers:
        if each_number.is_adjacent(symbols):
            sum_of_all_part_numbers += each_number.number

    return sum_of_all_part_numbers


def part2_example():
    return part1_example()


def part2(raw_input):
    numbers, symbols = process_parts(raw_input)

    number_map: dict[tuple, NumberInfo] = {}

    def populate_number_map(pos, num):
        number_map[pos] = num

    for each_number in numbers:
        [populate_number_map(position, each_number) for position in each_number.all_occupied_positions()]

    sum_of_gears = 0

    for key in symbols:
        if symbols[key] != '*':
            continue
        LOG.debug(f'Looking adjacent number for * at {key}')

        number_set = set()

        for y in range(key[0] - 1, key[0] + 2):
            for x in range(key[1] - 1, key[1] + 2):
                if (y, x) in number_map:
                    LOG.debug(f'\tAdding {number_map[(y, x)].number}')
                    number_set.add(number_map[(y, x)])

        if len(number_set) == 2:
            sum_of_gears += reduce(lambda a, b: a.number * b.number, number_set)

    return sum_of_gears
