elf = []
with open('input/day1.txt') as file:
    calories = []
    for line in file:
        if line == '\n':
            elf.append(calories)
            calories = []
        else:
            calories.append(int(line))


def part1():
    print(max(map(lambda e: sum(e), elf)))


def part2():
    print(sum(sorted(map(lambda e: sum(e), elf), reverse=True)[:3]))


if __name__ == '__main__':
    part1()
    part2()
