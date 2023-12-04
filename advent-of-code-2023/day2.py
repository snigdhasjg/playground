import logging
import re
from functools import reduce

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.CRITICAL)
DAY = 2
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = True


def part1_example():
    return """\
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def process_line(line):
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    pattern = re.compile('Game (\\d+): (.*)')
    search_result = pattern.search(line)
    game_id = int(search_result.group(1))
    all_game_set = []
    for each_game_set in search_result.group(2).split('; '):
        parsed_game_set = {}
        for each_ball in each_game_set.split(', '):
            ball_count_pattern = re.compile('(\\d+) (.*)')
            ball_count_search_result = ball_count_pattern.search(each_ball)
            parsed_game_set[ball_count_search_result.group(2)] = int(ball_count_search_result.group(1))
        all_game_set.append(parsed_game_set)

    return game_id, all_game_set


def part1(raw_input):
    possible_game_set = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    possible_game_ids_sum = 0

    def is_possible(game_set):
        for key in possible_game_set:
            if key in game_set and game_set[key] > possible_game_set[key]:
                return False
        return True

    for each_line in raw_input.splitlines():
        game_id, all_game_set = process_line(each_line)
        possible = True
        for each_game_set in all_game_set:
            if not is_possible(each_game_set):
                possible = False
        if possible:
            possible_game_ids_sum += game_id

    return possible_game_ids_sum


def part2_example():
    return part1_example()


def part2(raw_input):
    def minimum_combination(_all_game_set):
        combination = {}

        for game_set in all_game_set:
            for key in game_set:
                if key in combination:
                    combination[key] = max(combination[key], game_set[key])
                else:
                    combination[key] = game_set[key]

        return reduce(lambda x, y: x * y, combination.values())

    combination_power_sum = 0

    for each_line in raw_input.splitlines():
        _, all_game_set = process_line(each_line)
        combination_power_sum += minimum_combination(all_game_set)

    return combination_power_sum
