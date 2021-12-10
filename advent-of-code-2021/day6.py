with open('input/day6.txt') as file:
    input_seq = [[int(i) for i in line.split(',')] for line in file][0]


def calculate1(fish_timeline, count=0):
    if count == 256:
        return len(fish_timeline)
    new_fish = []
    for i in range(len(fish_timeline)):
        fish_age = fish_timeline[i]
        if fish_age == 0:
            new_fish.append(8)
            fish_age = 6
        else:
            fish_age -= 1
        fish_timeline[i] = fish_age
    # print('Day {}'.format(count), fish_timeline, new_fish)
    return calculate1(fish_timeline + new_fish, count + 1)


def calculate2(fish_timeline):
    dp = {}

    def calculate_each(single_fish_timeline, count=0):
        if count == 256:
            return 1

        try:
            return dp[(single_fish_timeline, count)]
        except KeyError:
            pass

        if single_fish_timeline == 0:
            timeline_count_ = calculate_each(6, count + 1) + calculate_each(8, count + 1)
        else:
            timeline_count_ = calculate_each(single_fish_timeline - 1, count + 1)

        dp[(single_fish_timeline, count)] = timeline_count_
        return timeline_count_

    return sum([calculate_each(i) for i in fish_timeline]), len(dp)


if __name__ == '__main__':
    print(calculate2(input_seq))
