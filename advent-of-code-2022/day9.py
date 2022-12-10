def parse_input():
    def parse_command(command_string):
        commands = command_string.split(' ')
        return commands[0], int(commands[1])

    with open('input/day9.txt') as file:
        return [parse_command(line.strip()) for line in file]


class Follower:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__position_visited = [(0, 0)]
        self.__follower: Follower = None

    def add_follower(self):
        if not self.__follower:
            self.__follower = Follower()
        else:
            raise 'Already one follower present'
        return self.__follower

    def follow(self, head_x, head_y):
        diff_x = abs(head_x - self.__x)
        diff_y = abs(head_y - self.__y)
        if diff_x <= 1 and diff_y <= 1:
            return

        if diff_x > 0:
            if head_x - self.__x > 0:
                self.__x += 1
            else:
                self.__x -= 1

        if diff_y > 0:
            if head_y - self.__y > 0:
                self.__y += 1
            else:
                self.__y -= 1

        if not self.__follower:
            # Only take a note of node visited to save space
            self.__position_visited.append((self.__x, self.__y))
        else:
            self.__follower.follow(self.__x, self.__y)

    def unique_position_visited(self):
        return len(set(self.__position_visited))


class Head:

    def __init__(self, follower: Follower):
        self.__x = 0
        self.__y = 0
        self.__follower = follower
        self.__movement_map = {
            'U': self.__up,
            'D': self.__down,
            'L': self.__left,
            'R': self.__right
        }

    def move(self, direction, move_count):
        for _ in range(move_count):
            self.__movement_map[direction]()
            self.__follower.follow(self.__x, self.__y)

    def __up(self):
        self.__x -= 1

    def __down(self):
        self.__x += 1

    def __left(self):
        self.__y -= 1

    def __right(self):
        self.__y += 1


def process(head: Head):
    commands = parse_input()
    for command in commands:
        head.move(command[0], command[1])


def part1():
    tail = Follower()
    head = Head(tail)

    process(head)

    print(tail.unique_position_visited())


def part2():
    follower1 = Follower()
    head = Head(follower1)
    tail = follower1 \
        .add_follower() \
        .add_follower() \
        .add_follower() \
        .add_follower() \
        .add_follower() \
        .add_follower() \
        .add_follower() \
        .add_follower()

    process(head)

    print(tail.unique_position_visited())


if __name__ == '__main__':
    part1()
    part2()
