import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.CRITICAL
DAY = 9
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = True


def part1_example():
    return """\
        0 3 6 9 12 15
        1 3 6 10 15 21
        10 13 16 21 30 45"""


def all_difference(sequence: list[int]):
    next_number = sequence[-1]
    prev_number = sequence[0]

    current_seq = sequence
    sign = -1
    while True:
        next_seq = []
        for idx in range(len(current_seq) - 1):
            next_seq.append(current_seq[idx + 1] - current_seq[idx])
        next_number += next_seq[-1]
        prev_number += (sign * next_seq[0])
        current_seq = next_seq
        sign *= -1

        if all(v == 0 for v in next_seq):
            break
    LOG.debug(f'For sequence {sequence}: previous number: {prev_number} & next number {next_number}')
    return prev_number, next_number


def part1(raw_input: str):
    sequences = [list(map(int, each_line.split(' '))) for each_line in raw_input.splitlines()]

    return sum(map(lambda x: x[1], map(all_difference, sequences)))


def part2_example():
    return part1_example()


def part2(raw_input: str):
    sequences = [list(map(int, each_line.split(' '))) for each_line in raw_input.splitlines()]

    return sum(map(lambda x: x[0], map(all_difference, sequences)))
