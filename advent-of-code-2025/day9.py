import logging
from itertools import chain, pairwise, combinations

import matplotlib.pyplot as plt

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.INFO
DAY = 9
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
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
    nodes = list(map(lambda x: tuple(map(int, x.split(","))), raw_input.splitlines()))

    no_of_red_tiles = len(nodes)

    max_area = -1

    for i in range(no_of_red_tiles):
        for j in range(i + 1, no_of_red_tiles):
            red_tile_1 = nodes[i]
            red_tile_2 = nodes[j]

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


def plot(parsed_input: list[tuple[int, int]]):
    xs, ys = zip(*parsed_input)

    plt.plot(xs, ys)  # line plot
    plt.scatter(xs, ys)  # or scatter plot
    plt.show()

class Rectangle:
    x_min: int
    x_max: int
    y_min: int
    y_max: int

    def __init__(self, p1: tuple[int, int], p2: tuple[int, int]) -> None:
        self.x_min, self.x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
        self.y_min, self.y_max = min(p1[1], p2[1]), max(p1[1], p2[1])

    def overlaps_with(self, other: 'Rectangle') -> bool:
        return not (
            self.x_max <= other.x_min
            or other.x_max <= self.x_min
            or self.y_max <= other.y_min
            or other.y_max <= self.y_min
        )

    def area(self) -> int:
        x_len = self.x_max - self.x_min + 1
        y_len = self.y_max - self.y_min + 1
        return x_len * y_len

def part2(raw_input: str):
    nodes = list(map(lambda x: tuple(map(int, x.split(","))), raw_input.splitlines()))

    no_of_red_tiles = len(nodes)
    LOG.debug("Length of input: %d", no_of_red_tiles)

    edges = [Rectangle(p, q) for p, q in chain(pairwise(nodes), [(nodes[-1], nodes[0])])]

    max_area = max(
        rectangle.area()
        for rectangle in (Rectangle(p, q) for p, q in combinations(nodes, 2))
        if not any(rectangle.overlaps_with(edge) for edge in edges)
    )

    return max_area

