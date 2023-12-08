import logging
import re
from functools import reduce

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG
DAY = 6
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = True


def part1_example():
    return """\
        Time:      7  15   30
        Distance:  9  40  200"""


def parse(raw_input: str):
    lines = raw_input.splitlines()
    times = list(map(int, re.split('\\s+', lines[0].lstrip('Time:').lstrip())))
    distances = list(map(int, re.split('\\s+', lines[1].lstrip('Distance:').lstrip())))

    return zip(times, distances)


def part1(raw_input):
    lines = raw_input.splitlines()
    times = list(map(int, re.split('\\s+', lines[0].lstrip('Time:').lstrip())))
    distances = list(map(int, re.split('\\s+', lines[1].lstrip('Distance:').lstrip())))

    win_probabilities = []
    for time, distance in zip(times, distances):
        counter = 0
        for unit_time in range(1, time):
            distance_covered = unit_time * (time - unit_time)
            if distance_covered > distance:
                counter += 1

        win_probabilities.append(counter)

    return reduce(lambda x, y: x * y, win_probabilities)


def part2_example():
    return part1_example()


def part2(raw_input: str):
    lines = raw_input.splitlines()
    time = int(lines[0].lstrip('Time:').replace(' ', ''))
    distance = int(lines[1].lstrip('Distance:').replace(' ', ''))

    counter = 0
    for unit_time in range(1, time):
        distance_covered = unit_time * (time - unit_time)
        if distance_covered > distance:
            counter += 1

    return counter
