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
        _temp_scanner_scan.append(tuple(map(lambda _x: int(_x), _line.split(','))))
    if _temp_scanner_scan and len(_temp_scanner_scan) is not 0:
        _all_scanner_scan.append(_temp_scanner_scan)

    return _all_scanner_scan


rotation_map = {
    0: lambda v: v,
    1: lambda v: (v[0], -v[2], v[1]),
    2: lambda v: (v[0], -v[1], -v[2]),
    3: lambda v: (v[0], v[2], -v[1]),

    4: lambda v: (-v[1], v[0], v[2]),
    5: lambda v: (v[2], v[0], v[1]),
    6: lambda v: (v[1], v[0], -v[2]),
    7: lambda v: (-v[2], v[0], -v[1]),

    8: lambda v: (-v[0], -v[1], v[2]),
    9: lambda v: (-v[0], -v[2], -v[1]),
    10: lambda v: (-v[0], v[1], -v[2]),
    11: lambda v: (-v[0], v[2], v[1]),

    12: lambda v: (v[1], -v[0], v[2]),
    13: lambda v: (v[2], -v[0], -v[1]),
    14: lambda v: (-v[1], -v[0], -v[2]),
    15: lambda v: (-v[2], -v[0], v[1]),

    16: lambda v: (-v[2], v[1], v[0]),
    17: lambda v: (v[1], v[2], v[0]),
    18: lambda v: (v[2], -v[1], v[0]),
    19: lambda v: (-v[1], -v[2], v[0]),

    20: lambda v: (-v[2], -v[1], -v[0]),
    21: lambda v: (-v[1], v[2], -v[0]),
    22: lambda v: (v[2], v[1], -v[0]),
    23: lambda v: (v[1], -v[2], -v[0])
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
            diff_selected = (selected_base[0] - selected[0],
                             selected_base[1] - selected[1],
                             selected_base[2] - selected[2])
            match_count = 1
            inner_loop_count = 1
            all_shifted = []
            for k in range(_new_scanner_length):
                if i == k:
                    continue
                inner_loop_count += 1
                other = _new_scanner[k]
                shifted = (other[0] + diff_selected[0],
                           other[1] + diff_selected[1],
                           other[2] + diff_selected[2])
                if is_present(indexed_scanner_dict, shifted):
                    match_count += 1
                else:
                    all_shifted.append(shifted)
                # if _base_scanner_length - inner_loop_count + 1 < 12 - match_count:  # total 25 - 19, 12 - match 5
                #     break
            if match_count >= 12:
                return all_shifted


def overlap(_base_scanner, _new_scanner):
    all_shifted = overlap_diff(_base_scanner, _new_scanner)
    if not all_shifted:
        return False
    [_base_scanner.append(_each) for _each in all_shifted]
    return True


def merge_if_possible(_base_scanner, _new_scanner):
    for rotation_id in range(24):
        if overlap(_base_scanner, rotate(_new_scanner, rotation_id)):
            return True
    return False


def all_possible_rotation(_all_scanner_scan: list):
    # base_scanner = _all_scanner_scan[0]
    # for _each in _all_scanner_scan[1:]:
    #     merge_if_possible(base_scanner, _each)
    # return base_scanner
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


if __name__ == '__main__':
    all_scanner_scan = read_input()
    rotation = all_possible_rotation(all_scanner_scan)
    # rotation.sort(key=lambda x: x[0])
    # for each in rotation:
    #     print('{},{},{}'.format(each[0], each[1], each[2]))
    print(len(rotation))

# if __name__ == '__main__':
#     temp = create_dict([[1, 2, 3], [1, 4, 5], [1, 2, 6]])
#     pass
