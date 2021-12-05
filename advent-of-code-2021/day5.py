def read_input():
    def read_line(_line):
        return [[int(num) for num in _each.split(',')] for _each in _line.split(' -> ')]

    with open('input/day5.txt') as file:
        return [read_line(line) for line in file]


dict_out = {}


def travel(_line):
    if _line[0][0] == _line[1][0]:
        # print('X fix', end='\t')
        start = _line[0][1]
        end = _line[1][1]
        if start > end:
            start, end = end, start

        for i in range(start, end + 1):
            try:
                dict_out[(_line[0][0], i)] += 1
            except KeyError:
                dict_out[(_line[0][0], i)] = 1

    elif _line[0][1] == _line[1][1]:
        # print('Y fix', end='\t')
        start = _line[0][0]
        end = _line[1][0]
        if start > end:
            start, end = end, start

        for i in range(start, end + 1):
            try:
                dict_out[(i, _line[0][1])] += 1
            except KeyError:
                dict_out[(i, _line[0][1])] = 1
    elif _line[0][0] == _line[0][1] and _line[1][0] == _line[1][1]:
        # print('X0 = Y0', end='\t')
        start = _line[0][0]
        end = _line[1][0]
        if start > end:
            start, end = end, start
        for i in range(start, end + 1):
            try:
                dict_out[(i, i)] += 1
            except KeyError:
                dict_out[(i, i)] = 1
    elif _line[0][0] + _line[0][1] == _line[1][0] + _line[1][1]:
        # print('X0 = Y1', end='\t')
        start = _line[0]
        end = _line[1]
        if start[0] > end[0]:
            start, end = end, start
        i = 0
        while [start[0] + i, start[1] - i] != end:
            # print(start[0] + i, start[1] - i)
            try:
                dict_out[(start[0] + i, start[1] - i)] += 1
            except KeyError:
                dict_out[(start[0] + i, start[1] - i)] = 1
            i += 1
        # print(end[0], end[1])
        try:
            dict_out[(end[0], end[1])] += 1
        except KeyError:
            dict_out[(end[0], end[1])] = 1
    elif _line[0][0] - _line[1][0] == _line[0][1] - _line[1][1]:
        start = _line[0]
        end = _line[1]
        if int(''.join([str(s) for s in start])) > int(''.join([str(s) for s in end])):
            start, end = end, start
        i = 0
        while [start[0] + i, start[1] + i] != end:
            try:
                dict_out[(start[0] + i, start[1] + i)] += 1
            except KeyError:
                dict_out[(start[0] + i, start[1] + i)] = 1
            i += 1
        # print(end[0], end[1])
        try:
            dict_out[(end[0], end[1])] += 1
        except KeyError:
            dict_out[(end[0], end[1])] = 1
    else:
        print('Nothing fix', end='\t')
        print(_line)


def run():
    for _line in read_input():
        travel(_line)
        # print(_line)
        # print_dict()
    print(len(list(filter(lambda x: x > 1, dict_out.values()))))


def print_dict():
    out = ''
    for i in range(10):
        for j in range(10):
            try:
                out += str(dict_out[(j, i)])
            except KeyError:
                out += '.'
        out += '\n'
    print(out)


if __name__ == '__main__':
    run()
