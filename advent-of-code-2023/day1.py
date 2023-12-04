import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.CRITICAL
DAY = 1
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = True


class PrefixTree:

    def __init__(self, value=None):
        self.value = value
        self.end_word = None
        self.next_characters: dict[str, 'PrefixTree'] = {}

    def search(self, line, start_idx=0) -> (bool, object):
        if start_idx >= len(line):
            LOG.warning("Word does not have enough character")
            return False, None
        current_char = line[start_idx]
        if current_char in self.next_characters:
            char_node = self.next_characters[current_char]
            if char_node.end_word is not None:
                return True, char_node.end_word
            return char_node.search(line, start_idx + 1)
        LOG.warning("No match found")
        return False, None

    def index(self, word, end_word=None) -> 'PrefixTree':
        if end_word is None:
            end_word = word
        node = self
        for each_char in word:
            node = node._next(each_char)
        node.end_word = end_word
        return self

    def _next(self, value) -> 'PrefixTree':
        if value not in self.next_characters:
            self.next_characters[value] = PrefixTree(value)
        return self.next_characters[value]


def part1_example():
    return """\
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet"""


def part1(raw_input):
    def parse_each(line):
        left_digit_found = False
        left_digit = None
        right_digit_found = False
        right_digit = None
        for idx in range(len(line)):
            each_char = line[idx]

            found, value = each_char.isdigit(), each_char

            if not left_digit_found:
                left_digit_found, left_digit = found, value
            elif found:
                right_digit_found, right_digit = found, value

        if left_digit_found and not right_digit_found:
            right_digit = left_digit

        number = int(left_digit + right_digit)
        LOG.debug(f'{line} translates to: {number}')
        return number

    return sum([parse_each(each_line) for each_line in raw_input.splitlines()])


def part2_example():
    return """\
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen"""


def part2(raw_input):
    digit_prefix_tree = (
        PrefixTree()
        .index('one', '1')
        .index('two', '2')
        .index('three', '3')
        .index('four', '4')
        .index('five', '5')
        .index('six', '6')
        .index('seven', '7')
        .index('eight', '8')
        .index('nine', '9')
    )

    def parse_each(line):
        left_digit_found = False
        left_digit = None
        right_digit_found = False
        right_digit = None
        for idx in range(len(line)):
            each_char = line[idx]

            if each_char.isdigit():
                found, value = True, each_char
            else:
                found, value = digit_prefix_tree.search(line, idx)

            if not left_digit_found:
                left_digit_found, left_digit = found, value
            elif found:
                right_digit_found, right_digit = found, value

        if left_digit_found and not right_digit_found:
            right_digit = left_digit

        number = int(left_digit + right_digit)
        LOG.debug(f'{line} translates to: {number}')
        return number

    return sum([parse_each(each_line) for each_line in raw_input.splitlines()])
