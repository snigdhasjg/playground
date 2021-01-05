# nhhmmss


def taking_input():
    _n1 = 1  # int(input())
    _n2 = 2  # int(input())

    return _n1, _n2


def get_limit(rev_index: str) -> int:
    _char_limit = {
        'f': 10,
        'e': 6,
        'd': 10,
        'c': 6,
        'b': 10,
        'a': 2
    }

    limit = _char_limit.get(rev_index)
    return limit


output = 1
n1, n2 = taking_input()
for n in range(n1, n2 + 1):
    number_format: str = str(n) + "abcdef"
    each_char_array = list(number_format)
    size: int = len(each_char_array)

    for i in range(0, size // 2):
        left = get_limit(each_char_array[i])
        left = left if left is not None else 1
        right = get_limit(each_char_array[-(i + 1)])
        right = right if right is not None else 1
        output *= min(left, right)

    if not size // 2 == size / 2:
        output *= get_limit(each_char_array[size // 2])

if __name__ == '__main__':
    print(output)
