with open('input/day9.txt') as file:
    input_seq = [[int(each) for each in list(line.strip())] for line in file]
    row_max = len(input_seq) - 1
    col_max = len(input_seq[0]) - 1


def check_with_neighbour(row, col, num) -> bool:
    if row > row_max or row < 0 or col > col_max or col < 0:
        return True
    return num < input_seq[row][col]


def get_small_number(row, col):
    num = input_seq[row][col]
    if check_with_neighbour(row + 1, col, num) and check_with_neighbour(row - 1, col, num) \
            and check_with_neighbour(row, col + 1, num) and check_with_neighbour(row, col - 1, num):
        return num + 1
    return 0


def find_all_small_nums():
    map_low_point = {}
    for i in range(row_max + 1):
        for j in range(col_max + 1):
            num = get_small_number(i, j)
            if num > 0:
                map_low_point[(i, j)] = num - 1
    return map_low_point


def go():
    visited = {}

    def go_spread(_row, _col):
        try:
            if visited[(_row, _col)]:
                return 0
        except KeyError:
            if _row > row_max or _row < 0 or _col > col_max or _col < 0:
                return 0
            visited[(_row, _col)] = True
            num = input_seq[_row][_col]
            if num == 9:
                return 0
            return 1 + go_spread(_row + 1, _col) + go_spread(_row - 1, _col) \
                   + go_spread(_row, _col + 1) + go_spread(_row, _col - 1)

    values = []
    small_nums_map = find_all_small_nums()
    print(small_nums_map)
    for row, col in small_nums_map:
        values.append(go_spread(row, col))
    values.sort(reverse=True)
    return values[0:3]


if __name__ == '__main__':
    print(go())
