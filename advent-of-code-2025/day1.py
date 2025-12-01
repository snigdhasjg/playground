import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.WARN
DAY = 1
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = True


def part1_example():
    return """\
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82"""


def part1(raw_input: str):
    current_position = 50
    counter = 0

    for instruction in raw_input.strip().splitlines():
        if instruction.startswith("L"):
            current_position -= int(instruction.removeprefix("L"))
        else:
            current_position += int(instruction.removeprefix("R"))

        current_position %= 100

        if current_position == 0:
            counter += 1

    return counter


def part2_example():
    return """\
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82"""


def part2(raw_input: str):
    current_position = 50
    counter = 0
    pass_through_0 = 0

    for instruction in raw_input.strip().splitlines():
        previous_position = current_position
        if instruction.startswith("L"):
            no_of_left_rotation = int(instruction.removeprefix("L"))
            before_mod = previous_position - no_of_left_rotation
            current_position = before_mod % 100
            no_of_times = abs((previous_position - no_of_left_rotation) // 100)
            pass_through_0 += no_of_times
            if previous_position == 0:
                pass_through_0 -= 1
            if current_position == 0:
                pass_through_0 += 1
        else:
            no_of_right_rotation = int(instruction.removeprefix("R"))
            before_mod = previous_position + no_of_right_rotation
            current_position = before_mod % 100
            no_of_times = (previous_position + no_of_right_rotation) // 100
            pass_through_0 += no_of_times

        LOG.info("%s: %s -> %s (%s): %s", instruction, previous_position, before_mod, current_position, pass_through_0 + counter)

    return counter + pass_through_0
