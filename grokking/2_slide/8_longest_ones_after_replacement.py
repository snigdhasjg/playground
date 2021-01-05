def find_longest_ones(input_array: list, k: int):
    input_string_length: int = len(input_array)

    output = 0
    start_idx = 0
    end_idx = -1
    max_repeat_letter_count = 0
    while True:
        end_idx += 1
        print(start_idx, end_idx, max_repeat_letter_count, output)
        if end_idx == input_string_length:
            break
        right_char = input_array[end_idx]
        if right_char == 1:
            max_repeat_letter_count += 1

        if end_idx - start_idx + 1 - max_repeat_letter_count > k:
            left_char = input_array[start_idx]
            if left_char == 1:
                max_repeat_letter_count -= 1
            start_idx += 1

        output = max(output, end_idx - start_idx + 1)

    return output


if __name__ == '__main__':
    print(find_longest_ones([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
