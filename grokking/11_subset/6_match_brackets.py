from typing import List


def match_bracket(_input_size: int) -> List[str]:
    output = []

    def __open_close_bracket(_limit: int, _open: int = 0, _close: int = 0, _level_bracket: str = None):
        if _level_bracket is None:
            _level_bracket = ''

        if _open == _close:
            if _open == _limit:
                output.append(_level_bracket)
                return
            __open_close_bracket(_limit, _open + 1, _close, _level_bracket + '(')
        else:
            if _open == _limit:
                __open_close_bracket(_limit, _open, _close + 1, _level_bracket + ')')
                return
            __open_close_bracket(_limit, _open + 1, _close, _level_bracket + '(')
            __open_close_bracket(_limit, _open, _close + 1, _level_bracket + ')')

    __open_close_bracket(_input_size)
    return output


if __name__ == '__main__':
    print(match_bracket(3))
