import logging
import textwrap
from datetime import datetime

from day5 import (
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
    start_time = datetime.now()
    print('Part 1:')
    print('\tExample: ', part1(textwrap.dedent(part1_example())))
    example_end_time = datetime.now()
    LOG.info(f'Part 1 Example took: {example_end_time - start_time}')
    if raw_input:
        print('\tData: ', part1(raw_input))
        data_end_time = datetime.now()
        LOG.info(f'Part 1 Data took: {data_end_time - example_end_time}')


def run_part2(raw_input):
    start_time = datetime.now()
    print('Part 2:')
    print('\tExample: ', part2(textwrap.dedent(part2_example())))
    example_end_time = datetime.now()
    LOG.info(f'Part 1 Example took: {example_end_time - start_time}')
    if raw_input:
        print('\tData: ', part2(raw_input))
        data_end_time = datetime.now()
        LOG.info(f'Part 1 Data took: {data_end_time - example_end_time}')


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
