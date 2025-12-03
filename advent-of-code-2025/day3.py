import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG
DAY = 3
DEVELOPMENT_PHASE = False
PART_1_ENABLE = False
PART_2_ENABLE = True


def part1_example():
    return """\
        987654321111111
        811111111111119
        234234234234278
        818181911112111"""


def find_max_part1(battery_bank: list[int]):
    highest = 0
    second_highest = 0

    for i in range(len(battery_bank) - 1):
        if battery_bank[i] > highest:
            highest = battery_bank[i]
            second_highest = battery_bank[i + 1]
        elif battery_bank[i + 1] > second_highest:
            second_highest = battery_bank[i + 1]

    number = 10 * highest + second_highest
    LOG.debug(f"For {battery_bank}: {number}")
    return number


def part1(raw_input: str):
    return sum(map(find_max_part1, (map(lambda x: list(map(int, list(x))), raw_input.splitlines()))))


def part2_example():
    return """\
        987654321111111
        811111111111119
        234234234234278
        818181911112111"""


def find_max_part2(battery_bank: list[int]):
    left_index = 0
    number = 0
    for i in range(12, 0, -1):
        highest = 0
        for j in range(left_index, len(battery_bank) - i +1):
            if battery_bank[j] > highest:
                highest = battery_bank[j]
                left_index = j + 1
        number = number * 10 + highest
    LOG.debug(f"For {battery_bank}: {number}")
    return number



def part2(raw_input: str):
    return sum(map(find_max_part2, (map(lambda x: list(map(int, list(x))), raw_input.splitlines()))))
