import math


def find_min_sum_length():  # N * (N+1) / 2
    input_array: list = [2, 1, 5, 2, 3, 2, 8, 9]

    def found_min_sum(slide_size, min_sum_limit=7):
        sliding_sum = 0
        for _idx in range(len(input_array)):
            if _idx < slide_size:
                sliding_sum += input_array[_idx]
            else:
                sliding_sum += input_array[_idx] - input_array[_idx - slide_size]
                if sliding_sum >= min_sum_limit:
                    return True
        return False

    for idx in range(1, len(input_array)):
        if found_min_sum(idx):
            return idx


def find_min_length_of_max_sum():
    input_array: list = [2, 1, 5, 1, 3, 2, 1, 1]

    min_sum_limit = 7
    sliding_sum = 0
    min_length = math.inf
    start_idx = 0
    end_idx = -1
    while True:
        # print(start_idx, end_idx, sliding_sum)
        if sliding_sum >= min_sum_limit:
            sliding_sum -= input_array[start_idx]
            len_of_slider = end_idx - start_idx + 1
            # print('hey', start_idx, end_idx, len_of_slider)
            if len_of_slider < min_length:
                min_length = len_of_slider
            start_idx += 1
        else:
            if end_idx == len(input_array) - 1:
                break
            end_idx += 1
            sliding_sum += input_array[end_idx]

    return min_length


if __name__ == '__main__':
    print(find_min_length_of_max_sum())
