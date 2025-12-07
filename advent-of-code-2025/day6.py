import logging
import re

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG
DAY = 6
DEVELOPMENT_PHASE = False
PART_1_ENABLE = False
PART_2_ENABLE = True


def part1_example():
    return """\
        123 328  51 64 
         45 64  387 23 
          6 98  215 314
        *   +   *   +  """


def part1(raw_input: str):
    math_homework = list(map(lambda x: re.split("\\s+", x.strip()), raw_input.splitlines()))

    final_result = 0
    for i in range(len(math_homework[0])):
        operation = math_homework[-1][i]
        result = 1 if operation == "*" else 0
        for j in range(len(math_homework) - 1):
            parsed_number = int(math_homework[j][i])
            result = result * parsed_number if operation == "*" else result + parsed_number

        LOG.debug(result)
        final_result += result

    return final_result


def part2_example():
    return """\
        123 328  51 64 
         45 64  387 23 
          6 98  215 314
        *   +   *   +  """


def part2(raw_input: str):
    math_homework = raw_input.splitlines()

    current_operation = None
    numbers = []
    final_result = 0

    def calculate():
        result = 1 if current_operation == "*" else 0
        for each_number in numbers:
            result = result * each_number if current_operation == "*" else result + each_number
        LOG.debug("%s %s", current_operation, numbers)
        return result

    for i in range(len(math_homework[0])):
        operation = math_homework[-1][i]
        if operation in {"*", "+"}:
            current_operation = operation

        number_str = ""
        for j in range(len(math_homework) - 1):
            number_char_str = math_homework[j][i]
            if number_char_str != " ":
                number_str += number_char_str

        if number_str != "":
            numbers.append(int(number_str))
        else:
            final_result += calculate()
            current_operation = None
            numbers = []
    final_result += calculate()

    return final_result