import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.INFO
DAY = 2
DEVELOPMENT_PHASE = True
PART_1_ENABLE = False
PART_2_ENABLE = True


class NumberRange:
    # 12001200 - 12991299
    # 12101210 - 12191219

    def __init__(self, start, end, half_length, number_prefix):
        self.start = start
        self.end = end
        self.half_length = half_length

        self.number_prefix = number_prefix
        self.number_prefix_str = str(self.number_prefix)
        self.number_prefix_len = len(self.number_prefix_str)
        self.suffix_fill_count = self.half_length - len(self.number_prefix_str)

        self.half_range_min = int(self.number_prefix_str + '0' * self.suffix_fill_count)
        self.half_range_max = int(self.number_prefix_str + '9' * self.suffix_fill_count)
        self.range_min = int(
            self.number_prefix_str + '0' * self.suffix_fill_count
            +
            self.number_prefix_str + '0' * self.suffix_fill_count
        )
        self.range_max = int(
            self.number_prefix_str + '9' * self.suffix_fill_count
            +
            self.number_prefix_str + '9' * self.suffix_fill_count
        )

    def is_valid_range(self):
        # start range_min range_max end
        return self.start <= self.range_min and self.range_max <= self.end

    def is_possible_range(self):
        # start range_min end range_max
        # range_min start range_max end
        # range_min start end range_max
        return (
                (self.start <= self.range_min <= self.end <= self.range_max) or
                (self.range_min <= self.start <= self.range_max <= self.end) or
                (self.range_min <= self.start <= self.end <= self.range_max)
        )

    def next_number_ranges(self) -> list['NumberRange']:
        if self.number_prefix_len >= self.half_length:
            return []
        return [
            NumberRange(self.start, self.end, self.half_length, int(self.number_prefix_str + str(i)))
            for i in range(0, 10)
        ]

    def sum(self):
        if self.number_prefix_len != self.half_length:
            return 0
        return self.range_sum()

    def range_sum(self):
        total_sum = 0
        for each_number in range(self.half_range_min, self.half_range_max + 1):
            full_number = int(f'{each_number}{each_number}')
            if self.start <= full_number <= self.end:
                total_sum += full_number
        return total_sum

    def __repr__(self):
        return f'{self.range_min}-{self.range_max} ({self.is_valid_range()},{self.is_possible_range()}) {self.sum()}'


def recurrence_each_range(number_range: NumberRange):
    LOG.debug(number_range)
    if number_range.is_valid_range():
        return number_range.range_sum()
    if not number_range.is_possible_range():
        return 0
    total_sum = number_range.sum()
    for each_number_range in number_range.next_number_ranges():
        total_sum += recurrence_each_range(each_number_range)
    return total_sum


def part1_example():
    return """\
        11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


def find_invalid_sum(start: str, end: str):
    invalid_number_lengths = list(filter(lambda x: x % 2 == 0, range(len(start), len(end) + 1)))
    LOG.info("For %s -> %s with length %s", start, end, invalid_number_lengths)
    total_sum = 0
    for each_length in invalid_number_lengths:
        possible_number_ranges = [NumberRange(int(start), int(end), int(each_length / 2), i) for i in range(1, 10)]
        for each_number_range in possible_number_ranges:
            total_sum += recurrence_each_range(each_number_range)
    return total_sum

def part1(raw_input: str):
    product_id_ranges = list(map(lambda x: x.split("-"), raw_input.split(",")))

    total_sum = 0
    for id_range in product_id_ranges:
        total_sum += find_invalid_sum(id_range[0], id_range[1])

    return total_sum


def part2_example():
    return """\
        multi
        line
        input"""


def part2(raw_input: str):
    pass
