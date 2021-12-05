from typing import List


def group_by(_input_list: List[int]):
    total_sum = sum(_input_list)
    if total_sum % 2 != 0:
        return None
    half_some = total_sum // 2

    def _group_by(_left: List[int], _left_sum: int, _right: List[int], _right_sum: int, _idx: int = 0) \
            -> (List[int], List[int]):

        if _idx == len(_input_list):
            if _left_sum == _right_sum:
                return _left, _right
            else:
                return None
        elif _left_sum > half_some or _right_sum > half_some:
            return None

        left_copy = _left[:]
        right_copy = _right[:]
        left_copy.append(_input_list[_idx])
        right_copy.append(_input_list[_idx])

        move_left = _group_by(left_copy, _left_sum + _input_list[_idx], _right, _right_sum, _idx + 1)
        if move_left:
            return move_left
        return _group_by(_left, _left_sum, right_copy, _right_sum + _input_list[_idx], _idx + 1)

    return _group_by([], 0, [], 0)


if __name__ == '__main__':
    print(group_by([1, 9, 7, 4, 3]))
