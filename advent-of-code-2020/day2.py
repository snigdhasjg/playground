class Password:

    def __init__(self, mandatory_char, lower_lmt, upper_lmt, password) -> None:
        self.password = password
        self.upper_lmt = upper_lmt
        self.lower_lmt = lower_lmt
        self.mandatory_char = mandatory_char

    def __str__(self) -> str:
        return f"{self.lower_lmt}-{self.upper_lmt} {self.mandatory_char}: {self.password}"

    def is_valid_part1(self) -> bool:
        count = 0
        for i in list(self.password):
            if self.mandatory_char == i:
                count += 1
        return self.upper_lmt >= count >= self.lower_lmt

    def is_valid_part2(self) -> bool:
        char_array = list(self.password)
        pos1 = char_array[self.lower_lmt - 1]
        pos2 = char_array[self.upper_lmt - 1]
        return (pos1 == self.mandatory_char) ^ (pos2 == self.mandatory_char)


def take_input():
    with open('input/day2.txt') as file:
        def split_password(line: str):
            _input = line.split(': ')
            policy = _input[0].split(' ')
            lmt = policy[0].split('-')
            password = Password(policy[1], int(lmt[0]), int(lmt[1]), _input[1])
            print(str(password), end='')
            return password

        return [split_password(line) for line in file]


def count_valid():
    count = 0
    for each in take_input():
        part_ = each.is_valid_part2()
        # print(part_)
        if part_:
            count += 1
    return count


if __name__ == '__main__':
    print(count_valid())
