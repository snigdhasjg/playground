with open('input/day11.txt') as file:
    input_seq = [[int(each) for each in line.strip()] for line in file]
    row_max = len(input_seq)
    col_max = len(input_seq[0])

delta_position = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def increase_energy(row, col):
    if row >= row_max or col >= col_max or row < 0 or col < 0:
        return
    num = input_seq[row][col]
    if num > 9:
        return
    num += 1
    input_seq[row][col] = num
    if num == 10:
        for d_row, d_col in delta_position:
            increase_energy(row + d_row, col + d_col)


def print_board():
    for i in range(row_max):
        for j in range(col_max):
            value = input_seq[i][j]
            if value == 0:
                print(' ', end='')
            else:
                print(value, end='')
        print()
    print()


def calculate_reset_flash():
    count = 0
    for i in range(row_max):
        for j in range(col_max):
            value = input_seq[i][j]
            if value == 10:
                count += 1
                input_seq[i][j] = 0
    return count


def iterate():
    step = 1
    while True:
        for i in range(row_max):
            for j in range(col_max):
                increase_energy(i, j)
        for i in range(row_max):
            for j in range(col_max):
                count = calculate_reset_flash()
                if count == 100:
                    return step
        step += 1
        # print_board()


if __name__ == '__main__':
    print(iterate())
