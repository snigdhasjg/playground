import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.INFO
DAY = 2
DEVELOPMENT_PHASE = True
PART_1_ENABLE = True
PART_2_ENABLE = True


class NumberRange:
    # 12001200 - 12991299
    # 12101210 - 12191219

    def __init__(self, start, end, max_repeat, number_prefix):
        self.start = start
        self.end = end
        self.max_repeat = max_repeat

        self.max_length = len(str(end)) // max_repeat
        self.number_prefix = number_prefix
        self.number_prefix_str = str(self.number_prefix)
        self.number_prefix_len = len(self.number_prefix_str)
        self.suffix_fill_count = self.max_length - len(self.number_prefix_str)

        self.half_range_min = int(self.number_prefix_str + '0' * self.suffix_fill_count)
        self.half_range_max = int(self.number_prefix_str + '9' * self.suffix_fill_count)
        self.range_min = int((self.number_prefix_str + '0' * self.suffix_fill_count) * self.max_repeat)
        self.range_max = int((self.number_prefix_str + '9' * self.suffix_fill_count) * self.max_repeat)

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
        if self.number_prefix_len >= self.max_length:
            return []
        return [
            NumberRange(self.start, self.end, self.max_repeat, int(self.number_prefix_str + str(i)))
            for i in range(0, 10)
        ]

    def range_sum(self):
        total_sum = 0
        for each_number in range(self.half_range_min, self.half_range_max + 1):
            full_number = int(str(each_number) * self.max_repeat)
            if self.start <= full_number <= self.end:
                total_sum += full_number
        return total_sum

    def invalid_ids(self) -> list[int]:
        ids = []
        for each_number in range(self.half_range_min, self.half_range_max + 1):
            full_number = int(str(each_number) * self.max_repeat)
            if self.start <= full_number <= self.end:
                ids.append(full_number)
        return ids

    def __repr__(self):
        return f'{self.range_min}-{self.range_max} ({self.is_valid_range()},{self.is_possible_range()})'


def recurrence_each_range(number_range: NumberRange) -> list[int]:
    # LOG.debug(number_range)
    if number_range.is_valid_range():
        return number_range.invalid_ids()
    if not number_range.is_possible_range():
        return []
    ids = []
    if number_range.number_prefix_len == number_range.max_length:
        ids.extend(number_range.invalid_ids())
    for each_number_range in number_range.next_number_ranges():
        ids.extend(recurrence_each_range(each_number_range))
    return ids


def part1_example():
    return """\
        11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


def find_invalid_sum_part1(start: str, end: str):
    LOG.info("For %s -> %s", start, end)
    ids = []
    possible_number_ranges = [NumberRange(int(start), int(end), 2, i) for i in range(1, 10)]
    for each_number_range in possible_number_ranges:
        ids.extend(recurrence_each_range(each_number_range))
    LOG.debug(ids)
    return sum(ids)


def part1(raw_input: str):
    product_id_ranges = list(map(lambda x: x.split("-"), raw_input.split(",")))

    total_sum = 0
    for id_range in product_id_ranges:
        total_sum += find_invalid_sum_part1(id_range[0], id_range[1])

    return total_sum


def part2_example():
    return """\
        11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


def find_invalid_sum_part2(start: str, end: str):
    LOG.info("For %s -> %s", start, end)
    ids = []
    for each_repeat in range(2, len(end) + 1):
        possible_number_ranges = [NumberRange(int(start), int(end), each_repeat, i) for i in range(1, 10)]
        for each_number_range in possible_number_ranges:
            ids.extend(recurrence_each_range(each_number_range))
    unique_ids = set(ids)
    LOG.debug(list(unique_ids))
    return sum(unique_ids)


def part2(raw_input: str):
    product_id_ranges = list(map(lambda x: x.split("-"), raw_input.split(",")))

    total_sum = 0
    for id_range in product_id_ranges:
        total_sum += find_invalid_sum_part2(id_range[0], id_range[1])

    return total_sum
