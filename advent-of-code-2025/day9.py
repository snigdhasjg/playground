import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG
DAY = 9
DEVELOPMENT_PHASE = True
PART_1_ENABLE = False
PART_2_ENABLE = True


def part1_example():
    return """\
        7,1
        11,1
        11,7
        9,7
        9,5
        2,5
        2,3
        7,3"""


def part1(raw_input: str):
    parsed_input = list(map(lambda x: tuple(map(int, x.split(","))), raw_input.splitlines()))

    no_of_red_tiles = len(parsed_input)

    max_area = -1

    for i in range(no_of_red_tiles):
        for j in range(i + 1, no_of_red_tiles):
            red_tile_1 = parsed_input[i]
            red_tile_2 = parsed_input[j]

            diff_in_x = abs(red_tile_1[0] - red_tile_2[0]) + 1
            diff_in_y = abs(red_tile_1[1] - red_tile_2[1]) + 1

            area = diff_in_x * diff_in_y

            LOG.debug("%s %s: %s", red_tile_1, red_tile_2, area)

            max_area = max(max_area, area)

    return max_area


def part2_example():
    return """\
        7,1
        11,1
        11,7
        9,7
        9,5
        2,5
        2,3
        7,3"""


def part2(raw_input: str):
    parsed_input = list(map(lambda x: tuple(map(int, x.split(","))), raw_input.splitlines()))

    no_of_red_tiles = len(parsed_input)

    
