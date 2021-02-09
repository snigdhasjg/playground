import pprint
from typing import List

pp = pprint.PrettyPrinter(indent=4)


def find_weight_top_down(_weight_list: List[int], _profit_list: List[int], _capacity: int) -> int:
    if len(_weight_list) != len(_profit_list):
        raise ValueError
    total_item = len(_weight_list)
    func_state = {}

    def _find_weight(_idx: int = 0, _weight_left: int = _capacity, _profit: int = 0) -> int:
        state_get = func_state.get((_weight_left, _idx))
        if state_get:
            print("vola", _weight_left, _idx, state_get)
            return state_get
        if _weight_left < 0:
            func_state[(_weight_left, _idx)] = _profit
            return 0
        if _idx == total_item:
            func_state[(_weight_left, _idx)] = _profit
            return _profit
        state_value = max(_find_weight(_idx + 1, _weight_left - _weight_list[_idx], _profit + _profit_list[_idx]),
                          _find_weight(_idx + 1, _weight_left, _profit))
        func_state[(_weight_left, _idx)] = state_value
        return state_value

    weight = _find_weight()
    pp.pprint(func_state)
    return weight


def find_weight_bottom_up(_weight_list: List[int], _profit_list: List[int], _capacity: int) -> int:
    if len(_weight_list) != len(_profit_list):
        raise ValueError
    total_item = len(_weight_list)
    func_state = {}

    def _find_weight(_idx: int = 0, _weight_left: int = _capacity) -> int:
        state_get = func_state.get((_weight_left, _idx))
        if state_get:
            print("vola", _weight_left, _idx, state_get)
            return state_get
        if _idx == total_item:
            return 0
        if _weight_left - _weight_list[_idx] < 0:
            current_profit = 0
        else:
            current_profit = _profit_list[_idx] + _find_weight(_idx + 1, _weight_left - _weight_list[_idx])
        state_value = max(current_profit, _find_weight(_idx + 1, _weight_left))
        func_state[(_weight_left, _idx)] = state_value
        return state_value

    weight = _find_weight()
    pp.pprint(func_state)
    return weight


if __name__ == '__main__':
    print(find_weight_bottom_up([1, 2, 3, 5], [1, 6, 10, 16], 66))
