with open('input/day2.txt') as file:
    input = [line.strip().split(' ') for line in file]

decode_map_1 = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors',
}

decode_map_2 = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

loose_map = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}

win_map = {
    'Rock': 'Paper',
    'Paper': 'Scissors',
    'Scissors': 'Rock'
}

point_map = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}


def calculate_score_1(opponent_draw, mine_draw):
    if opponent_draw == mine_draw:
        return 3 + point_map[mine_draw]
    if (opponent_draw == 'Scissors' and mine_draw == 'Rock') or \
            (opponent_draw == 'Paper' and mine_draw == 'Scissors') or \
            (opponent_draw == 'Rock' and mine_draw == 'Paper'):
        return 6 + point_map[mine_draw]
    return 0 + point_map[mine_draw]


def calculate_score_2(opponent_draw, my_command):
    # print(opponent_draw, my_command)
    if my_command == 'lose':
        return calculate_score_1(opponent_draw, loose_map[opponent_draw])
    if my_command == 'win':
        return calculate_score_1(opponent_draw, win_map[opponent_draw])
    return calculate_score_1(opponent_draw, opponent_draw)


def part1():
    print(sum([calculate_score_1(decode_map_1[each_pair[0]], decode_map_1[each_pair[1]]) for each_pair in input]))


def part2():
    print(sum([calculate_score_2(decode_map_2[each_pair[0]], decode_map_2[each_pair[1]]) for each_pair in input]))


if __name__ == '__main__':
    part2()
