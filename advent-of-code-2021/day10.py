with open('input/day10.txt') as file:
    input_seq = [list(line.strip()) for line in file]

open_close_map = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}

close_score_map = {
    '{': 3,
    '[': 2,
    '(': 1,
    '<': 4
}


def match(opening_bracket, closing_bracket):
    return open_close_map[opening_bracket] == closing_bracket


def read(input_str_arr):
    stack = []
    score = 0
    for each in input_str_arr:
        try:
            _ = open_close_map[each]
            stack.insert(0, each)
        except KeyError:
            opening_bracket = stack.pop(0)
            if not match(opening_bracket, each):
                return 0
    while len(stack) > 0:
        opening_bracket = stack.pop(0)
        score = score * 5 + close_score_map[opening_bracket]
    return score


def find_score():
    seq_ = list(filter(lambda x: x > 0, [read(each) for each in input_seq]))
    seq_.sort()
    print(len(seq_))
    return seq_[int(len(seq_)/2)]


if __name__ == '__main__':
    print(find_score())
