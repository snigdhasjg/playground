import logging
import textwrap

from day8 import (
    LOG_LEVEL,
    DAY,
    DEVELOPMENT_PHASE,
    PART_1_ENABLE, PART_2_ENABLE,
    part1_example, part2_example,
    part1, part2
)

logging.basicConfig(level=LOG_LEVEL, format='%(message)s')
LOG = logging.getLogger(__name__)


def get_data():
    if DEVELOPMENT_PHASE:
        return None

    import aocd
    return aocd.get_data(day=DAY, year=2023)


def run_part1(raw_input):
    print('Part 1:')
    print('\tExample: ', part1(textwrap.dedent(part1_example())))
    if raw_input:
        print('\tData: ', part1(raw_input))


def run_part2(raw_input):
    print('Part 2:')
    print('\tExample: ', part2(textwrap.dedent(part2_example())))
    if raw_input:
        print('\tData: ', part2(raw_input))


def main():
    data = get_data()

    print(f'DAY {DAY}\n--------------')

    if PART_1_ENABLE:
        run_part1(data)
    print('--------------')
    if PART_2_ENABLE:
        run_part2(data)


if __name__ == '__main__':
    main()
