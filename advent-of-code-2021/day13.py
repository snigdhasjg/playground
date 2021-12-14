def read_data():
    with open('input/day13.txt') as file:
        read_all_point = False
        points = []
        fold_ins = []
        for line in file:
            _strip = line.strip()
            if not read_all_point:
                if _strip == '':
                    read_all_point = True
                    continue
                _split = _strip.split(',')
                points.append((int(_split[0]), int(_split[1])))
            else:
                _fold = _strip.split('fold along ')[1].split('=')
                fold_ins.append((_fold[0], int(_fold[1])))
    return points, fold_ins


def fold_y(_points, position):
    for i in range(len(_points)):
        point = _points[i]
        if point[1] == position:
            point = None
        elif point[1] > position:
            point = (point[0], position * 2 - point[1])
        _points[i] = point
    out = []
    [out.append(x) for x in _points if x and x not in out]
    return out


def fold_x(_points, _position):
    for i in range(len(_points)):
        point = _points[i]
        if point[0] == _position:
            point = None
        elif point[0] > _position:
            point = (_position * 2 - point[0], point[1])
        _points[i] = point
    out = []
    [out.append(x) for x in _points if x and x not in out]
    return out


def print_points(points):
    max_x = -1
    max_y = -1
    for x, y in points:
        max_y = max(max_y, y)
        max_x = max(max_x, x)
    base = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in points:
        base[y][x] = '#'

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(base[y][x], end='')
        print()
    print()


def fold():
    _points, fold_ins = read_data()
    for axis, position in fold_ins:
        if axis == 'x':
            _points = fold_x(_points, position)
        elif axis == 'y':
            _points = fold_y(_points, position)
        print(axis, position, len(_points))
    return _points


if __name__ == '__main__':
    print_points(fold())
