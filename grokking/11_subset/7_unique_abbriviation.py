from typing import List


def find_abbreviation(_input_str: str) -> List[str]:
    input_arr = list(_input_str)
    output = []

    def __get_abbreviation(_index: int = 0, _level_abbreviation: str = '', _last_type: type = None):
        if _index == len(input_arr):
            output.append(_level_abbreviation)
            return

        current_char = input_arr[_index]
        __get_abbreviation(_index + 1, _level_abbreviation + current_char, str)
        if _last_type is int:
            value = int(_level_abbreviation[-1])
            __get_abbreviation(_index + 1, _level_abbreviation[:-1] + str(value+1), int)
        else:
            __get_abbreviation(_index + 1, _level_abbreviation + '1', int)

    __get_abbreviation()
    return output


if __name__ == '__main__':
    print(find_abbreviation('ANUSHREE'))
