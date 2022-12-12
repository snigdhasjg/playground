import math


def read_data():
    with open('input/day14.txt') as file:
        _input = [line.strip() for line in file]
    input_str = list(_input[0])
    relations = {}
    for line in _input[2:]:
        line_split = line.split(' -> ')
        relations[line_split[0]] = line_split[1]
    return input_str, relations


def replace_one_step():
    input_str, relations = read_data()
    dp = {}

    def _replace(set_of_two_char, index=20):
        try:
            index_ = dp[(set_of_two_char, index)]
            print('hit', set_of_two_char, index)
            return index_
        except KeyError:
            value = relations[set_of_two_char]
            if index == 1:
                return value

            _joined = '{}{}{}'.format(_replace('{}{}'.format(set_of_two_char[0], value), index - 1),
                                      value,
                                      _replace('{}{}'.format(value, set_of_two_char[1]), index - 1))
            dp[(set_of_two_char, index)] = _joined
            return _joined

    out = []
    for i in range(1, len(input_str)):
        out.append(input_str[i - 1])
        out.append(_replace(''.join(input_str[i - 1: i + 1])))
    out.append(input_str[-1])

    joined = ''.join(out)
    return joined


def run_multiple_times():
    input_str = replace_one_step()

    unique = []
    [unique.append(i) for i in input_str if i not in unique]

    _max_count = -1
    _min_count = math.inf
    for each in unique:
        count = input_str.count(each)
        _max_count = max(_max_count, count)
        _min_count = min(_min_count, count)

    return _max_count - _min_count


class Counter:
    def __init__(self):
        self.count = {}

    def max_min_diff(self):
        _max_count = -1
        _min_count = math.inf
        for key in self.count:
            value = self.count[key]
            _max_count = max(_max_count, value)
            _min_count = min(_min_count, value)

        return _max_count - _min_count

    def take_count(self, letter, count=1):
        if letter in self.count:
            self.count[letter] += count
        else:
            self.count[letter] = count

    def __add__(self, other):
        _add_counter = Counter()
        for key in self.count:
            _add_counter.take_count(key, self.count[key])
        for key in other.add_item_count:
            _add_counter.take_count(key, other.add_item_count[key])

        return _add_counter


def count_max_min():
    input_str, relations = read_data()
    dp = {}

    def _replace(set_of_two_char, index=40):
        if (set_of_two_char, index) in dp:
            return dp[(set_of_two_char, index)]
        value = relations[set_of_two_char]
        _current_counter = Counter()
        _current_counter.take_count(value)
        if index == 1:
            dp[(set_of_two_char, index)] = _current_counter
            return _current_counter

        _current_counter += \
            _replace(set_of_two_char[0] + value, index - 1) + _replace(value + set_of_two_char[1], index - 1)
        dp[(set_of_two_char, index)] = _current_counter
        return _current_counter

    _first_counter = Counter()
    for i in range(1, len(input_str)):
        _first_counter.take_count(input_str[i - 1])
        _first_counter += _replace(''.join(input_str[i - 1: i + 1]))
    _first_counter.take_count(input_str[-1])

    return _first_counter


if __name__ == '__main__':
    print(count_max_min().max_min_diff())
