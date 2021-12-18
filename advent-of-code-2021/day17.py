import math


def find_range_x(_trench):
    left_target, right_target = _trench[0][0], _trench[0][1]
    range_x = []
    counter = 0
    cumulative_sum = 0
    while cumulative_sum <= right_target:
        if left_target <= cumulative_sum:
            range_x.append(counter)
        counter += 1
        cumulative_sum += counter

    return range_x


def draw(initial_x, initial_y, _trench):
    y_min = _trench[1][0]
    position = {(0, 0): 'S'}
    decrement_x, decrement_y = 1, 1
    temp_x, temp_y = initial_x, initial_y
    y_max = -math.inf
    while temp_y >= y_min:
        y_max = max(y_max, temp_y)
        position[(temp_x, temp_y)] = '#'
        temp_x += initial_x - decrement_x
        temp_y += initial_y - decrement_y
        if initial_x is not decrement_x:
            decrement_x += 1
        decrement_y += 1
    x_min, x_max = 0, _trench[0][1]

    base_map = [['.' for _ in range(x_max - x_min + 1)] for _ in range(y_max - y_min + 1)]
    # print('y.len', len(base_map))
    # print('x.len', len(base_map[0]))
    # print('y.max', y_max)

    for y in range(abs(_trench[1][1] - y_max), abs(_trench[1][0] - y_max) + 1):
        for x in range(_trench[0][0], _trench[0][1] + 1):
            base_map[y][x] = 'T'

    for x, y in position:
        try:
            base_map[abs(y - y_max)][x] = position[(x, y)]
        except IndexError:
            pass

    return '\n'.join([''.join(line) for line in base_map])


def compare_diff_y(_trench):
    x_range = 6  # [7, 8, 9, 10, 11]
    for y in range(9, 10):
        print('Power', x_range, y)
        print(draw(x_range, y, _trench))
        print()


def get_range(no_of_jumps, _trench):
    left_target, right_target = _trench[0][0], _trench[0][1]
    temp = (no_of_jumps * (no_of_jumps - 1)) / 2
    min_range = math.ceil((left_target + temp) / no_of_jumps)
    max_range = math.floor((right_target + temp) / no_of_jumps)
    return [i for i in range(min_range, max_range + 1)]


def find_min_number(_trench):
    left_target = _trench[0][0]
    counter = 1
    cumulative_sum = 0
    while True:
        cumulative_sum += counter
        if cumulative_sum >= left_target:
            return counter
        counter += 1


def is_falling(x, y, _trench):
    position_x, position_y = 0, 0
    decrement = 0
    while True:
        new_position_x, new_position_y = position_x if x - decrement < 0 else position_x + x - decrement,\
                                         position_y + y - decrement
        if _trench[0][0] <= new_position_x <= _trench[0][1] and _trench[1][0] <= new_position_y <= _trench[1][1]:
            return True
        if new_position_x > _trench[0][1]:
            return False
        if new_position_y < _trench[1][0]:
            return False
        decrement += 1
        position_x, position_y = new_position_x, new_position_y


def find_points_per_x(x, _trench):
    y_max = abs(_trench[1][0]) - 1
    y_min = math.floor(_trench[1][0] / 2)
    count = 0
    y = y_max
    while y > y_min:
        if is_falling(x, y, _trench):
            # print(x, y)
            count += 1
        y -= 1
    return count


def find_points(_trench):
    direct_hit = (_trench[0][1] - _trench[0][0] + 1) * (abs(_trench[1][0]) - abs(_trench[1][1]) + 1)

    min_x = find_min_number(_trench)
    max_x = math.ceil(_trench[0][1] / 2)
    for x in range(min_x, max_x + 1):
        direct_hit += find_points_per_x(x, _trench)

    return direct_hit


if __name__ == '__main__':
    # trench = [[20, 30], [-10, -5]]
    trench = [[25, 67], [-260, -200]]
    print(find_points(trench))
