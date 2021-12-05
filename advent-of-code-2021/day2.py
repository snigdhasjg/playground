def split_command_dir(line):
    line_split = line.strip().split(' ')
    return line_split[0], int(line_split[1])


with open('input/day2.txt') as file:
    report = [split_command_dir(line) for line in file]

initial_depth = [0, 0, 0]


def apply_command(_command, _direction):
    if _command == 'forward':
        initial_depth[0] += _direction
        initial_depth[1] += initial_depth[2] * _direction
    elif _command == 'down':
        initial_depth[2] += _direction
    elif _command == 'up':
        initial_depth[2] -= _direction


for (command, direction) in report:
    apply_command(command, direction)
    # print(command, direction)
    # print(initial_depth)

print(initial_depth[0] * initial_depth[1])

if __name__ == '__main__':
    pass
