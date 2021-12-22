def main1():
    initial_pos = [9, 6]
    score = [0, 0]

    def next_no_of_pos(_prev_no_of_pos):
        if _prev_no_of_pos == 0:
            return 9
        return _prev_no_of_pos - 1

    def next_pos(_current, _next_no_of_pos):
        return (_current + _next_no_of_pos - 1) % 10 + 1

    prev_no_of_pos = 7
    player_selected = 0
    count = 0
    while score[0] < 1000 and score[1] < 1000:
        player_pos = initial_pos[player_selected]
        no_of_pos = next_no_of_pos(prev_no_of_pos)
        new_pos = next_pos(player_pos, no_of_pos)
        initial_pos[player_selected] = new_pos
        score[player_selected] += new_pos

        prev_no_of_pos = no_of_pos
        # print(player_selected + 1, new_pos, score)
        player_selected = (player_selected + 1) % 2
        count += 3

    return min(score[0], score[1]) * count


import itertools


def main2():
    initial_pos = (9, 6)

    addition = list(map(lambda x: x[0] + x[1] + x[2], itertools.product(range(1, 4), repeat=3)))
    addition.sort()
    # print(addition)
    permutation = list(map(lambda x: (x[0], len(list(x[1]))), itertools.groupby(addition)))

    # print(permutation)

    def next_pos(_current, _next_no_of_pos):
        return (_current + _next_no_of_pos - 1) % 10 + 1

    winning_score = 9

    # dp = {}

    def roll(position, score, dice_total=0, player_idx=1):
        if player_idx == 0:
            position = (next_pos(position[0], dice_total), position[1])
            score = (score[0] + position[0], score[1])
        else:
            position = (position[0], next_pos(position[1], dice_total))
            score = (score[0], score[1] + position[1])
        if score[0] >= winning_score or score[1] >= winning_score:
            if score[0] > score[1]:  # TODO change
                return 1
            return 0
        new_player_idx = (player_idx + 1) % 2

        # if (position, score) in dp:
        #     return dp[(position, score)]

        total = 0
        for _dice_total, times in permutation:
            total += times * roll(position, score, _dice_total, new_player_idx)
        # dp[(position, score)] = total
        return total

    return roll(initial_pos, (0, -initial_pos[1]))


if __name__ == '__main__':
    print(main2())
