def find_repeat_string(s: str, k: int):
    if s is None or s is '':
        return 0
    input_string: list = list(s)
    input_string_length: int = len(input_string)
    char_map_for_index: dict = dict()

    output = 0
    start_idx = 0
    end_idx = -1
    max_repeat_letter_count = 0
    while True:
        end_idx += 1
        print(start_idx, end_idx, max_repeat_letter_count, output, char_map_for_index)
        if end_idx == input_string_length:
            break
        right_char = input_string[end_idx]
        if right_char in char_map_for_index:
            char_map_for_index[right_char] += 1
        else:
            char_map_for_index[right_char] = 1
        max_repeat_letter_count = max(max_repeat_letter_count, char_map_for_index[right_char])

        if end_idx - start_idx + 1 - max_repeat_letter_count > k:
            left_char = input_string[start_idx]
            char_map_for_index[left_char] -= 1
            start_idx += 1

        output = max(output, end_idx - start_idx + 1)

    return output


if __name__ == '__main__':
    print(find_repeat_string('eecddeaaaa', 2))
