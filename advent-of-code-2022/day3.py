def get_character_weight(character):
    ascii_value = ord(character)
    if ascii_value >= 97:
        return ascii_value - 96
    return ascii_value - 64 + 26


def part1():
    def find_common(rucksack):
        left, right = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:].strip()
        return list(set(left) & set(right))[0]

    with open('input/day3.txt') as file:
        weight = sum([get_character_weight(find_common(line)) for line in file])
        print(weight)


def part2():
    with open('input/day3.txt') as file:
        rucksack = [line.strip() for line in file]

    grouped = [list(set(rucksack[i]) & set(rucksack[i + 1]) & set(rucksack[i + 2]))[0] for i in range(0, len(rucksack), 3)]

    weight = sum([get_character_weight(each) for each in grouped])

    print(weight)


if __name__ == '__main__':
    part2()
