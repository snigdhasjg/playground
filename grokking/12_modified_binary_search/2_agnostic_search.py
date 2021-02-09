from typing import List, Callable


def find_number(_input_list: List[int], _input_num: int) -> int:
    def __decide_which_way() -> Callable[[int], bool]:
        if len(_input_list) <= 1:
            return lambda _: True
        if _input_list[0] < _input_list[1]:
            return lambda _current_value: _current_value > _input_num
        return lambda _current_value: _current_value < _input_num

    __should_go_left: Callable[[int], bool] = __decide_which_way()

    def __search_binary(_left: int = 0, _right: int = len(_input_list) - 1):
        if _left > _right:
            return -1
        _idx: int = (_left + _right) // 2

        if _input_list[_idx] == _input_num:
            return _idx

        if __should_go_left(_input_list[_idx]):
            return __search_binary(_left, _idx - 1)
        else:
            return __search_binary(_idx + 1, _right)

    return __search_binary()


if __name__ == '__main__':
    print(find_number([], 4))
