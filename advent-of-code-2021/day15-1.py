import sys
from heapq import heapify, heappush, heappop

sys.setrecursionlimit(500 * 500)


def read_data():
    with open('input/day15.txt') as file:
        return [[int(i) for i in list(line.strip())] for line in file]


class PositionWithDistance:
    def __init__(self, position, distance):
        self.row_pos = position[0]
        self.col_pos = position[1]
        self.position = position
        self.distance = distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __eq__(self, other):
        return self.distance == other.distance


def travel():
    path = read_data()

    def get_value(row_actual, col_actual):
        row = row_actual % 100
        col = col_actual % 100
        row_times = int(row_actual / 100)
        col_times = int(col_actual / 100)
        value = path[row][col]

        new_value = value + row_times + col_times
        new_new_value = new_value % 100
        if new_value is not new_new_value:
            return new_new_value + 1
        return new_new_value

    row_max = len(path) * 5 - 1
    col_max = len(path[0]) * 5 - 1
    delta_position = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    heap = []
    heapify(heap)
    heappush(heap, PositionWithDistance((0, 0), 0))
    visited = {}

    while len(heap) is not 0:
        poll: PositionWithDistance = heappop(heap)
        if poll.row_pos == row_max and poll.col_pos == col_max:
            return poll.distance
        visited[poll.position] = poll.distance

        for d_row, d_col in delta_position:
            new_row = poll.row_pos + d_row
            new_col = poll.col_pos + d_col
            if 0 <= new_row <= row_max and 0 <= new_col <= col_max and (new_row, new_col) not in visited:
                heappush(heap,
                         PositionWithDistance((new_row, new_col), poll.distance + get_value(new_row, new_col)))
    return 0


if __name__ == '__main__':
    print(travel())
