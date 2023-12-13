import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.CRITICAL
DAY = 13
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = True


def part1_example():
    return """\
        #.##..##.
        ..#.##.#.
        ##......#
        ##......#
        ..#.##.#.
        ..##..##.
        #.#.##.#.
        
        #...##..#
        #....#..#
        ..##..###
        #####.##.
        #####.##.
        ..##..###
        #....#..#"""


class Terrain:
    def __init__(self, pattern: str):
        raw_rows = pattern.splitlines()
        raw_columns = [''] * len(raw_rows[0])

        for each_line in raw_rows:
            for idx, each_char in enumerate(each_line):
                raw_columns[idx] += each_char

        self.rows = list(map(lambda x: int(x, 2), map(lambda y: y.replace('#', '1').replace('.', '0'), raw_rows)))
        self.columns = list(map(lambda x: int(x, 2), map(lambda y: y.replace('#', '1').replace('.', '0'), raw_columns)))

    @staticmethod
    def find_match(orientation: list[int]):
        matching_indexes = []
        max_length = len(orientation)
        for idx in range(max_length - 1):
            if orientation[idx] == orientation[idx + 1]:
                matching_indexes.append(idx)

        LOG.debug(matching_indexes)

        for each_centre_match in matching_indexes:
            steps_to_check = min(each_centre_match, max_length - each_centre_match - 2)
            matched = True
            for step in range(1, steps_to_check + 1):
                if orientation[each_centre_match - step] != orientation[each_centre_match + 1 + step]:
                    matched = False
                    break
            if matched:
                return each_centre_match + 1
        return 0

    @staticmethod
    def find_match_with_smudge(orientation: list[int]):
        matching_indexes = []
        max_length = len(orientation)
        for idx in range(max_length - 1):
            if orientation[idx] == orientation[idx + 1]:
                matching_indexes.append((idx, False))
            else:
                x_or_result = orientation[idx] ^ orientation[idx + 1]
                if x_or_result.bit_count() == 1:
                    LOG.debug(f'Found initial smudge between idx {idx} & {idx + 1}')
                    matching_indexes.append((idx, True))

        LOG.debug(matching_indexes)

        for each_centre_match, found_smudge in matching_indexes:
            steps_to_check = min(each_centre_match, max_length - each_centre_match - 2)
            matched = True
            found_smudge_all = found_smudge
            for step in range(1, steps_to_check + 1):
                if orientation[each_centre_match - step] != orientation[each_centre_match + 1 + step]:
                    if found_smudge_all:
                        matched = False
                        break
                    else:
                        x_or_result = orientation[each_centre_match - step] ^ orientation[each_centre_match + 1 + step]
                        if x_or_result.bit_count() == 1:
                            LOG.debug(f'Found smudge at idx {each_centre_match - step}, {each_centre_match + 1 + step}')
                            found_smudge_all = True
                        else:
                            matched = False
                            break
            if matched and found_smudge_all:
                return each_centre_match + 1
        return 0

    def horizontal(self, with_smudge=False):
        """2 or more row"""
        LOG.debug(f'Rows: {self.rows}')

        matched_rows = self.find_match_with_smudge(self.rows) if with_smudge else self.find_match(self.rows)
        LOG.debug(f'Match for position {100 * matched_rows}')
        return matched_rows * 100

    def vertical(self, with_smudge=False):
        """2 or more columns"""
        LOG.debug(f'Columns: {self.columns}')

        matched_rows = self.find_match_with_smudge(self.columns) if with_smudge else self.find_match(self.columns)
        LOG.debug(f'Match for position {matched_rows}')
        return matched_rows

    def __repr__(self):
        return f'Rows: {self.rows}\nColumns: {self.columns}'


def part1(raw_input: str):
    summary = 0
    for each_pattern in raw_input.split('\n\n'):
        terrain = Terrain(each_pattern)

        score = terrain.horizontal() + terrain.vertical()
        if score == 0:
            LOG.error(f'Zero for :\n{each_pattern}')
        summary += score

    return summary


def part2_example():
    return part1_example()


def part2(raw_input: str):
    summary = 0
    for each_pattern in raw_input.split('\n\n'):
        terrain = Terrain(each_pattern)

        score = terrain.horizontal(True) + terrain.vertical(True)
        if score == 0:
            LOG.error(f'Zero for :\n{each_pattern}')
        summary += score

    return summary
