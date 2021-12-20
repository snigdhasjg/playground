def read_input():
    _all_scanner_scan = []
    _temp_scanner_scan = None
    for _line in open("input/day19.txt").read().splitlines():
        if _line[:3] == '---':
            _temp_scanner_scan = []
            continue
        if _line == '':
            _all_scanner_scan.append(_temp_scanner_scan)
            continue
        _line += ',0'
        _temp_scanner_scan.append(tuple(map(lambda _x: int(_x), _line.split(','))))
    if _temp_scanner_scan and len(_temp_scanner_scan) is not 0:
        _all_scanner_scan.append(_temp_scanner_scan)

    return _all_scanner_scan


rotation_map = {
    0: lambda v: v,
    1: lambda v: (v[0], -v[2], v[1], v[3]),
    2: lambda v: (v[0], -v[1], -v[2], v[3]),
    3: lambda v: (v[0], v[2], -v[1], v[3]),

    4: lambda v: (-v[1], v[0], v[2], v[3]),
    5: lambda v: (v[2], v[0], v[1], v[3]),
    6: lambda v: (v[1], v[0], -v[2], v[3]),
    7: lambda v: (-v[2], v[0], -v[1], v[3]),

    8: lambda v: (-v[0], -v[1], v[2], v[3]),
    9: lambda v: (-v[0], -v[2], -v[1], v[3]),
    10: lambda v: (-v[0], v[1], -v[2], v[3]),
    11: lambda v: (-v[0], v[2], v[1], v[3]),

    12: lambda v: (v[1], -v[0], v[2], v[3]),
    13: lambda v: (v[2], -v[0], -v[1], v[3]),
    14: lambda v: (-v[1], -v[0], -v[2], v[3]),
    15: lambda v: (-v[2], -v[0], v[1], v[3]),

    16: lambda v: (-v[2], v[1], v[0], v[3]),
    17: lambda v: (v[1], v[2], v[0], v[3]),
    18: lambda v: (v[2], -v[1], v[0], v[3]),
    19: lambda v: (-v[1], -v[2], v[0], v[3]),

    20: lambda v: (-v[2], -v[1], -v[0], v[3]),
    21: lambda v: (-v[1], v[2], -v[0], v[3]),
    22: lambda v: (v[2], v[1], -v[0], v[3]),
    23: lambda v: (v[1], -v[2], -v[0], v[3]),
}


def create_dict(_base_scanner):
    out = {}
    for each in _base_scanner:
        level_1 = out[each[0]] if each[0] in out else {}
        level_2 = level_1[each[1]] if each[1] in level_1 else {}
        level_3 = level_2[each[2]] if each[2] in level_2 else True
        level_2[each[2]] = level_3
        level_1[each[1]] = level_2
        out[each[0]] = level_1

    return out


def is_present(indexed_scanner_dict, position):
    if position[0] in indexed_scanner_dict:
        level_1 = indexed_scanner_dict[position[0]]
        if position[1] in level_1:
            if position[2] in level_1[position[1]]:
                return True
    return False


def rotate(_scanner_scan, rotation_id):
    rotation_func = rotation_map[rotation_id]
    return [rotation_func(_each) for _each in _scanner_scan]


def overlap_diff(_base_scanner, _new_scanner):
    _new_scanner_length = len(_new_scanner)
    _base_scanner_length = len(_base_scanner)
    indexed_scanner_dict = create_dict(_base_scanner)
    for i in range(_new_scanner_length):
        selected = _new_scanner[i]
        for j in range(_base_scanner_length):
            selected_base = _base_scanner[j]
            if selected_base[3] == 1:
                continue
            diff_selected = (selected_base[0] - selected[0],
                             selected_base[1] - selected[1],
                             selected_base[2] - selected[2], 1)
            match_count = 1
            all_shifted = []
            for k in range(_new_scanner_length):
                if i == k:
                    continue
                other = _new_scanner[k]
                shifted = (other[0] + diff_selected[0],
                           other[1] + diff_selected[1],
                           other[2] + diff_selected[2], other[3])
                if is_present(indexed_scanner_dict, shifted):
                    match_count += 1
                else:
                    all_shifted.append(shifted)
            if match_count >= 12:
                return all_shifted, diff_selected


def overlap(_base_scanner, _new_scanner):
    temp = overlap_diff(_base_scanner, _new_scanner)
    if not temp:
        return False
    all_shifted, diff_selected = temp[0], temp[1]
    [_base_scanner.append(_each) for _each in all_shifted]
    _base_scanner.append(diff_selected)
    return True


def merge_if_possible(_base_scanner, _new_scanner):
    for rotation_id in range(24):
        if overlap(_base_scanner, rotate(_new_scanner, rotation_id)):
            return True
    return False


def all_possible_rotation(_all_scanner_scan: list):
    i, j = 0, 1
    while len(_all_scanner_scan) is not 1:
        current_length = len(_all_scanner_scan)
        if i == j:
            i += 1
            j = i + 1
        if i >= current_length:
            i = i % current_length
        if j >= current_length:
            j = j % current_length
        if i > j:
            i, j = j, i
        print('Size', current_length)
        print(i, j)
        f_scanner = _all_scanner_scan[i]
        s_scanner = _all_scanner_scan[j]
        if merge_if_possible(f_scanner, s_scanner):
            _all_scanner_scan.pop(j)
            i += 1
            j = i + 1
        else:
            j += 1
    return _all_scanner_scan[0]


def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + abs(pos1[2] - pos2[2])


def find_max_manhattan_distance(_all_scanner):
    scanner_pos = _all_scanner
    no_of_scanner = len(scanner_pos)
    max_distance = -1
    for i in range(no_of_scanner):
        for j in range(no_of_scanner):
            if i == j:
                continue
            max_distance = max(max_distance, manhattan_distance(scanner_pos[i], scanner_pos[j]))
    return max_distance


if __name__ == '__main__':
    all_scanner_scan = read_input()
    rotation = all_possible_rotation(all_scanner_scan)
    all_scanner = list(filter(lambda x: x[3] == 1, rotation))
    all_scanner.append((0, 0, 0, 1))

    print(find_max_manhattan_distance(all_scanner))
    print(all_scanner)
    print(len(rotation) - len(all_scanner))

