import logging
import re

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.CRITICAL
DAY = 4
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = True


def part1_example():
    return """\
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def parse_raw_input(raw_input):
    def parse_each_line(line: str):
        scratch_card = re.split(':\\s+', line)[1]
        scratch_card_split = scratch_card.split(' | ')
        winning_numbers = set(re.split('\\s+', scratch_card_split[0]))
        draw_numbers = re.split('\\s+', scratch_card_split[1])

        lucky_numbers = [x for x in draw_numbers if x in winning_numbers]

        return len(lucky_numbers)

    parsed_input = [parse_each_line(each_line) for each_line in raw_input.splitlines()]
    return parsed_input


def part1(raw_input):
    numbers_of_win = parse_raw_input(raw_input)

    return sum([2 ** (x - 1) for x in numbers_of_win if x > 0])


def part2_example():
    return part1_example()


def part2(raw_input):
    numbers_of_win = parse_raw_input(raw_input)

    LOG.debug(numbers_of_win)

    initial_count = [1] * len(numbers_of_win)
    LOG.debug(initial_count)

    for idx, count in enumerate(numbers_of_win):
        initial_count[idx + 1:idx + count + 1] = [
            x + initial_count[idx] for x in initial_count[idx + 1:idx + count + 1]
        ]
        LOG.debug(initial_count)

    return sum(initial_count)
