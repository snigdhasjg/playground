import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.CRITICAL
DAY = 11
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = True


def part1_example():
    return """\
        ...#......
        .......#..
        #.........
        ..........
        ......#...
        .#........
        .........#
        ..........
        .......#..
        #...#....."""


def part1(raw_input: str):
    return process_galaxy(raw_input)


def process_galaxy(raw_input, empty_space_len=1):
    galaxies_map = []
    max_y, max_x = len(raw_input.splitlines()), len(raw_input.splitlines()[0])
    found_galaxy_rows = [False] * max_y
    found_galaxy_columns = [False] * max_x
    for idx_y, each_line in enumerate(raw_input.splitlines()):
        for idx_x, each_char in enumerate(each_line):
            if each_char == '#':
                galaxies_map.append((idx_y, idx_x))
                found_galaxy_rows[idx_y] = True
                found_galaxy_columns[idx_x] = True
    LOG.debug(f'Row: \t{found_galaxy_rows}')
    LOG.debug(f'Column: {found_galaxy_columns}')
    sortest_paths_sum = 0
    for i in range(len(galaxies_map)):
        for j in range(i + 1, len(galaxies_map)):
            a_galaxy = galaxies_map[i]
            other_galaxy = galaxies_map[j]
            LOG.debug(f'\t1: {a_galaxy}, 2: {other_galaxy}')

            length = 0

            start_y, end_y = (a_galaxy[0], other_galaxy[0]) \
                if a_galaxy[0] <= other_galaxy[0] \
                else (other_galaxy[0], a_galaxy[0])
            length += end_y - start_y
            for row in range(start_y + 1, end_y):
                if not found_galaxy_rows[row]:
                    LOG.debug(f'\tExpand galaxy at row {row}')
                    length += empty_space_len

            start_x, end_x = (a_galaxy[1], other_galaxy[1]) \
                if a_galaxy[1] <= other_galaxy[1] \
                else (other_galaxy[1], a_galaxy[1])
            length += end_x - start_x
            for column in range(start_x + 1, end_x):
                if not found_galaxy_columns[column]:
                    LOG.debug(f'\tExpand galaxy at column {column}')
                    length += empty_space_len

            LOG.debug(f'Sortest path between g{i + 1} & g{j + 1}: {length}')
            sortest_paths_sum += length
    return sortest_paths_sum


def part2_example():
    return part1_example()


def part2(raw_input: str):
    return process_galaxy(raw_input, 999999)
