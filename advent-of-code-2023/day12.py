import logging
from dataclasses import dataclass

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG
DAY = 12
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = True


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
        dp = {}

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
            dp_index = (condition_idx, group_idx, group_count, current_char)

            if dp_index in dp:
                return dp[dp_index]
            if current_char == '#':
                if group_idx < len(self.contiguous_group) and group_count + 1 <= self.contiguous_group[group_idx]:
                    dp_value = find_arrangement(condition_idx + 1, group_idx, group_count + 1, current_char)
                    dp[dp_index] = dp_value
                    return dp_value
                dp[dp_index] = 0
                return 0
            elif current_char == '.':
                if prev_char == '.' or prev_char is None:
                    dp_value = find_arrangement(condition_idx + 1, group_idx, 0, current_char)
                    dp[dp_index] = dp_value
                    return dp_value
                elif group_idx < len(self.contiguous_group) and self.contiguous_group[group_idx] == group_count:
                    dp_value = find_arrangement(condition_idx + 1, group_idx + 1, 0, current_char)
                    dp[dp_index] = dp_value
                    return dp_value
                dp[dp_index] = 0
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
                dp[dp_index] = permutation
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
    return part1_example()


def part2(raw_input: str):
    sum_of_permutations = 0
    for each_line in raw_input.splitlines():
        line_split = each_line.split(' ')
        contiguous_group = list(map(int, line_split[1].split(','))) * 5
        spring_condition = '?'.join([line_split[0]] * 5)

        info = Information(spring_condition, contiguous_group)
        sum_of_permutations += info.arrangement()

    return sum_of_permutations
