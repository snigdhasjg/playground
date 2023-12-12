import logging
import re
from dataclasses import dataclass

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG
DAY = 12
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = False


def part1_example():

    return """\
        ???.### 1,1,3
        .??..??...?##. 1,1,3
        ?#?#?#?#?#?#?#? 1,3,1,6
        ????.#...#... 4,1,1
        ????.######..#####. 1,6,5
        ?###???????? 3,2,1"""


@dataclass
class Information:
    spring_condition: str
    contiguous_group: list[int]

    def arrangement(self):
        LOG.debug(self)

        def find_arrangement(condition_idx=0, group_idx=0, group_count=0, prev_char=None):
            if condition_idx == len(self.spring_condition):
                if prev_char == '.':
                    if group_idx == len(self.contiguous_group):
                        return 1
                    return 0
                if group_idx == len(self.contiguous_group):
                    if group_count == 0:
                        return 1
                if group_idx < len(self.contiguous_group) - 1:
                    return 0
                if self.contiguous_group[group_idx] == group_count:
                    return 1
                return 0

            current_char = self.spring_condition[condition_idx]
            if current_char == '#':
                if group_idx < len(self.contiguous_group) and group_count + 1 <= self.contiguous_group[group_idx]:
                    return find_arrangement(condition_idx + 1, group_idx, group_count + 1, current_char)
                return 0
            elif current_char == '.':
                if prev_char == '.' or prev_char is None:
                    return find_arrangement(condition_idx + 1, group_idx, 0, current_char)
                elif group_idx < len(self.contiguous_group) and self.contiguous_group[group_idx] == group_count:
                    return find_arrangement(condition_idx + 1, group_idx + 1, 0, current_char)
                return 0
            else:  # Char is `?`
                # Lets say its a `#`
                permutation = 0
                if group_idx < len(self.contiguous_group) and group_count + 1 <= self.contiguous_group[group_idx]:
                    permutation += find_arrangement(condition_idx + 1, group_idx, group_count + 1, '#')
                # Lets say its a `.`
                if prev_char == '.' or prev_char is None:
                    permutation += find_arrangement(condition_idx + 1, group_idx, 0, '.')
                elif group_idx < len(self.contiguous_group) and self.contiguous_group[group_idx] == group_count:
                    permutation += find_arrangement(condition_idx + 1, group_idx + 1, 0, '.')
                return permutation

        return find_arrangement()

    def __repr__(self):
        return f'{self.spring_condition} -> {self.contiguous_group}'


def part1(raw_input: str):
    sum_of_permutations = 0
    for each_line in raw_input.splitlines():
        line_split = each_line.split(' ')
        contiguous_group = list(map(int, line_split[1].split(',')))

        info = Information(line_split[0], contiguous_group)
        sum_of_permutations += info.arrangement()

    return sum_of_permutations


def part2_example():
    return """\
        multi
        line
        input"""


def part2(raw_input: str):
    pass
