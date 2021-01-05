def find_no_repeat_string(s: str):
    input_string: list = list(s)
    char_map_for_index: dict = dict()
    max_distinct_length = -1
    start_idx = 0
    for end_idx in range(len(input_string)):
        current_char = input_string[end_idx]
        if current_char in char_map_for_index:
            start_idx = max(char_map_for_index[current_char] + 1, start_idx)
        char_map_for_index[current_char] = end_idx
        max_distinct_length = max(end_idx - start_idx + 1, max_distinct_length)

    return max_distinct_length


if __name__ == '__main__':
    print(find_no_repeat_string('abccabcbb'))
