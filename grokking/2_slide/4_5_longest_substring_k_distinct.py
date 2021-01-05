input_string: list = list('ABCAC')
char_map_for_count: dict = dict()


def find_longest_distinct(k: int = 2):
    max_distinct_length = -1
    start_idx = 0
    end_idx = -1
    new_char = 0
    while True:
        print(start_idx, end_idx, char_map_for_count)
        if new_char <= k:
            len_of_slider = end_idx - start_idx + 1
            print(len_of_slider)
            if max_distinct_length < len_of_slider:
                max_distinct_length = len_of_slider
            if end_idx == len(input_string) - 1:
                break
            end_idx += 1
            current_char = input_string[end_idx]
            if current_char in char_map_for_count:
                char_map_for_count[current_char] += 1
            else:
                new_char += 1
                char_map_for_count[current_char] = 1
        else:
            if start_idx > end_idx:
                break
            current_char = input_string[start_idx]
            start_idx += 1
            if current_char in char_map_for_count:
                if char_map_for_count[current_char] == 1:
                    del char_map_for_count[current_char]
                    new_char -= 1
                else:
                    char_map_for_count[current_char] -= - 1
    return max_distinct_length


if __name__ == '__main__':
    print(find_longest_distinct())
