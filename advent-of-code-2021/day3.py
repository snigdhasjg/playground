with open('input/day3.txt') as file:
    report = [list(line.strip()) for line in file]


# count = [0] * len(report[0])
#
# for each_line in report:
#     for idx, each_num in enumerate(each_line):
#         if each_num == '1':
#             count[idx] += 1
#
# gamma_max = ''
# epsilon_min = ''
#
# max_num = len(report)
# for each in count:
#     ratio = each / max_num
#     if ratio > 0.5:
#         gamma_max += '1'
#         epsilon_min += '0'
#     elif ratio < 0.5:
#         gamma_max += '0'
#         epsilon_min += '1'
#     else:
#         print('Go ****')
#
# print(int(gamma_max, 2) * int(epsilon_min, 2))

def count(filter_array: list, index):
    _count = 0

    for each_line in filter_array:
        if each_line[index] == '1':
            _count += 1

    max_num = len(filter_array)
    ratio = _count / max_num
    if ratio >= 0.5:
        return '1', '0'
    else:
        return '0', '1'


def oxygen_max(_array: list, index: int = 0):
    if len(_array) == 1:
        return _array[0]

    _max, _ = count(_array, index)
    return oxygen_max(list(filter(lambda x: x[index] == _max, _array)), index + 1)


def co2_min(_array: list, index: int = 0):
    if len(_array) == 1:
        return _array[0]

    _, _min = count(_array, index)
    return co2_min(list(filter(lambda x: x[index] == _min, _array)), index + 1)


print(int(''.join(oxygen_max(report)), 2) * int(''.join(co2_min(report)), 2))

# for each_line in report:
if __name__ == '__main__':
    pass
