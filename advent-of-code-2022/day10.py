def parse_input():
    def parse_command(command: str):
        if command == 'noop':
            return 'noop', 0
        value_to_add = int(command.removeprefix('addx '))
        return 'addx', value_to_add

    with open('input/day10.txt') as file:
        return [parse_command(line.strip()) for line in file]


class Signal:
    def __init__(self):
        self.__value = 1
        self.__cost = -1
        self.__positions = [20, 60, 100, 140, 180, 220]
        self.strength = 0
        self.__crt = [['?' for _ in range(40)] for _ in range(6)]

    def add(self, value, operation):
        def common():
            self.__cost += 1
            self.__crt[self.__cost // 40][self.__cost % 40] \
                = ('#' if abs(self.__value - (self.__cost % 40)) <= 1 else ' ')
            if self.__cost in self.__positions:
                self.strength += self.__value * self.__cost
            # print('Start {}: {}'.format(self.__cost+1, self.__value - (self.__cost % 40)))

        if operation == 'noop':
            common()
        if operation == 'addx':
            common()
            common()
            self.__value += value

    def crt_board(self):
        return '\n'.join([''.join(each) for each in self.__crt])


def process():
    signal = Signal()

    for cost_with_command in parse_input():
        signal.add(cost_with_command[1], cost_with_command[0])

    print('part1: ', signal.strength)
    print('part2:')
    print(signal.crt_board())


if __name__ == '__main__':
    process()
