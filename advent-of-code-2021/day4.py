def take_input():
    def read_5x5(_lines):
        out = []
        for _line in _lines:
            each_line = []
            for _each in _line.split(' '):
                if _each != '':
                    each_line.append([int(_each.strip()), False])
            out.append(each_line)
        return out

    with open('input/day4.txt') as file:
        lines = [line.strip() for line in file]
    input_random = [int(each) for each in lines[0].split(',')]
    _boards = []
    i = 2
    while i < len(lines):
        _boards.append([read_5x5(lines[i:i + 5]), -1])
        i += 6

    return input_random, _boards


random_number, boards = take_input()


def print_board(board):
    for line in board:
        out = ''
        for each in line:
            if each[1]:
                out += '"' + str(each[0]) + '" '
            else:
                out += ' ' + str(each[0]) + '  '
        print(out)
    print()


def mark_number(board, number):
    for line in board:
        for each in line:
            if each[0] == number:
                each[1] = True


def check_column(board):
    for y in range(5):
        count = 0
        for x in range(5):
            if board[x][y][1]:
                count += 1
        if count == 5:
            return sum_of_unmark(board)

    return -1


def check_row(board):
    for x in range(5):
        count = 0
        for y in range(5):
            if board[x][y][1]:
                count += 1
        if count == 5:
            return sum_of_unmark(board)

    return -1


def sum_of_unmark(board):
    _sum = 0
    for x in board:
        for y in x:
            if not y[1]:
                _sum += y[0]
    return _sum


def check():
    win = 0
    for num in random_number:
        for board in boards:
            if board[1] >= 0:
                continue
            mark_number(board[0], num)
            _sum1 = check_column(board[0])
            _found = False

            if _sum1 >= 0:
                # print(num, boards)
                board[1] = _sum1 * num
                print_board(board[0])
                win += 1
            else:
                _sum2 = check_row(board[0])
                if _sum2 >= 0:
                    # print(num, boards)
                    board[1] = _sum2 * num
                    print_board(board[0])
                    win += 1

            if win == len(boards):
                return board[1]
                # print(num, boards)

    return -1


if __name__ == '__main__':
    print(check())
