import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG
DAY = 5
DEVELOPMENT_PHASE = False
PART_1_ENABLE = False
PART_2_ENABLE = True


def part1_example():
    return """\
        3-5
        10-14
        16-20
        12-18
        
        1
        5
        8
        11
        17
        32"""


def part1(raw_input: str):
    raw_input_split = raw_input.split("\n\n")
    fresh_ingredient_ranges = list(map(lambda x: tuple(map(int, x.split("-"))), raw_input_split[0].splitlines()))
    available_ingredients = list(map(int, raw_input_split[1].splitlines()))

    def is_fresh(ingredient_id):
        for range_min, range_max in fresh_ingredient_ranges:
            if range_min <= ingredient_id <= range_max:
                return True
        return False

    return len(list(filter(is_fresh, available_ingredients)))


def part2_example():
    return """\
        3-5
        10-14
        16-20
        12-18
        
        1
        5
        8
        11
        17
        32"""


def part2(raw_input: str):
    raw_input_split = raw_input.split("\n\n")
    fresh_ingredient_ranges = list(map(lambda x: tuple(map(int, x.split("-"))), raw_input_split[0].splitlines()))

    def unique_ranges(range1: tuple[int, int], range2: tuple[int, int]):
        # min1 min2 max1 max2
        if range1[0] <= range2[0] <= range1[1] <= range2[1]:
            # range2[0] - range1[0]
            return [(range1[0], range2[0] - 1)]
        # min2 min1 max2 max1
        elif range2[0] <= range1[0] <= range2[1] <= range1[1]:
            # range1[1] - range2[1]
            return [(range2[1] + 1, range1[1])]
        # min1 min2 max2 max1
        elif range1[0] <= range2[0] <= range2[1] <= range1[1]:
            # (range2[0] - range1[0]) + (range1[1] - range2[1])
            return [(range1[0], range2[0] - 1), (range2[1] + 1, range1[1])]
        # min2 min1 max1 max2
        elif range2[0] <= range1[0] <= range1[1] <= range2[1]:
            # 0
            return []
        # min1 max1 min2 max2
        # min2 max2 min1 max1
        # range1[1] < range2[0] or range2[1] < range1[0]
        # range1[1] - range1[0] + 1
        return [range1]

    count = 0
    for i in range(len(fresh_ingredient_ranges)):
        current_ranges = [fresh_ingredient_ranges[i]]
        for j in range(i + 1, len(fresh_ingredient_ranges)):
            range_to_compare = fresh_ingredient_ranges[j]
            new_current_ranges = []
            for current_range in current_ranges:
                new_current_ranges.extend(unique_ranges(current_range, range_to_compare))
            current_ranges = new_current_ranges

        LOG.debug("For range %s, new updated ranges %s", fresh_ingredient_ranges[i], current_ranges)
        for current_range in current_ranges:
            count += current_range[1] - current_range[0] + 1

    return count
