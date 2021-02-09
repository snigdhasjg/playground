def getSmallestString(n: int, k: int) -> str:
    output = ['a'] * n
    find_weight_bottom_up(n, n, k, output)
    return ''.join(output)


def find_weight_bottom_up(n: int, _n: int, _k: int, output) -> (str, int):
    if _n == 0:
        return _k
    remaining_k = find_weight_bottom_up(n, _n - 1, _k - 1, output)
    if remaining_k == 0:
        return 0
    remaining_k = remaining_k + 1
    if remaining_k > 26:
        output[n - _n] = 'z'
        return remaining_k - 26
    output[n - _n] = chr(remaining_k + 96)
    return 0


if __name__ == '__main__':
    print(getSmallestString(5, 31))
