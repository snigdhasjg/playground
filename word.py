number_in_word = {
    0: ('zero', 2),
    1: ('one', 2),
    2: ('two', 1),
    3: ('three', 2),
    4: ('four', 2),
    5: ('five', 2),
    6: ('six', 1),
    7: ('seven', 2),
    8: ('eight', 2),
    9: ('nine', 2),
    10: ('ten', 1),
    11: ('eleven', 3),
    12: ('twelve', 2),
    13: ('thirteen', 3),
    14: ('fourteen', 4),
    15: ('fifteen', 3),
    16: ('sixteen', 3),
    17: ('seventeen', 4),
    18: ('eighteen', 4),
    19: ('nineteen', 4),
    20: ('twenty', 1),
    21: ('twentyone', 3),
    22: ('twentytwo', 2),
    23: ('twentythree', 3),
    24: ('twentyfour', 3),
    25: ('twentyfive', 3),
    26: ('twentysix', 2),
    27: ('twentyseven', 3),
    28: ('twentyeight', 3),
    29: ('twentynine', 3),
    30: ('thirty', 1),
    31: ('thirtyone', 3),
    32: ('thirtytwo', 2),
    33: ('thirtythree', 3),
    34: ('thirtyfour', 3),
    35: ('thirtyfive', 3),
    36: ('thirtysix', 2),
    37: ('thirtyseven', 3),
    38: ('thirtyeight', 3),
    39: ('thirtynine', 3),
    40: ('forty', 1),
    41: ('fortyone', 3),
    42: ('fortytwo', 2),
    43: ('fortythree', 3),
    44: ('fortyfour', 3),
    45: ('fortyfive', 3),
    46: ('fortysix', 2),
    47: ('fortyseven', 3),
    48: ('fortyeight', 3),
    49: ('fortynine', 3),
    50: ('fifty', 1),
    51: ('fiftyone', 3),
    52: ('fiftytwo', 2),
    53: ('fiftythree', 3),
    54: ('fiftyfour', 3),
    55: ('fiftyfive', 3),
    56: ('fiftysix', 2),
    57: ('fiftyseven', 3),
    58: ('fiftyeight', 3),
    59: ('fiftynine', 3),
    60: ('sixty', 1),
    61: ('sixtyone', 3),
    62: ('sixtytwo', 2),
    63: ('sixtythree', 3),
    64: ('sixtyfour', 3),
    65: ('sixtyfive', 3),
    66: ('sixtysix', 2),
    67: ('sixtyseven', 3),
    68: ('sixtyeight', 3),
    69: ('sixtynine', 3),
    70: ('seventy', 2),
    71: ('seventyone', 4),
    72: ('seventytwo', 3),
    73: ('seventythree', 4),
    74: ('seventyfour', 4),
    75: ('seventyfive', 4),
    76: ('seventysix', 3),
    77: ('seventyseven', 4),
    78: ('seventyeight', 4),
    79: ('seventynine', 4),
    80: ('eighty', 2),
    81: ('eightyone', 4),
    82: ('eightytwo', 3),
    83: ('eightythree', 4),
    84: ('eightyfour', 4),
    85: ('eightyfive', 4),
    86: ('eightysix', 3),
    87: ('eightyseven', 4),
    88: ('eightyeight', 4),
    89: ('eightynine', 4),
    90: ('ninety', 2),
    91: ('ninetyone', 4),
    92: ('ninetytwo', 3),
    93: ('ninetythree', 4),
    94: ('ninetyfour', 4),
    95: ('ninetyfive', 4),
    96: ('ninetysix', 3),
    97: ('ninetyseven', 4),
    98: ('ninetyeight', 4),
    99: ('ninetynine', 4),
    100: ('hundred', 2)
}


def print_dict_with_no_of_vowel():
    def get_no_of_vowel(word: str):
        vowel = ['a', 'e', 'i', 'o', 'u']
        total = 0
        for c in list(word):
            if c in vowel:
                total += 1
        return total

    for key in number_in_word.keys():
        value = number_in_word[key][0]
        print('{}: (\'{}\', {}),'.format(key, value, get_no_of_vowel(value)))


def sum_of_vowel(list_of_input_number: list):
    _sum = 0
    for num in list_of_input_number:
        no_of_vowel = number_in_word[num][1]
        _sum += no_of_vowel

    return _sum


def get_no_pair(list_of_input_number: list):
    _sum = sum_of_vowel(list_of_input_number)
    filtered_list_eligible_for_pair = list(filter(lambda _num: _num < _sum, list_of_input_number))
    size_of_filtered_list = len(filtered_list_eligible_for_pair)

    # print(filtered_list_eligible_for_pair)
    # print(_sum)

    visited = set()
    total_pair = 0
    for i in range(0, size_of_filtered_list):
        _num_i = filtered_list_eligible_for_pair[i]
        for j in range(0, size_of_filtered_list):
            if i == j:
                continue
            _num_j = filtered_list_eligible_for_pair[j]
            if _num_i + _num_j == _sum:
                if _num_i not in visited:
                    total_pair += 1
                    visited.add(_num_i)
                    visited.add(_num_j)
    if total_pair > 100:
        return "greater 100"
    return number_in_word.get(total_pair)[0]


def take_input():
    input()  # ignore this as no need
    input_number_in_string = input()
    input_list = list(map(int, input_number_in_string.split(" ")))
    return input_list


if __name__ == '__main__':
    pass

import universal_orbit
