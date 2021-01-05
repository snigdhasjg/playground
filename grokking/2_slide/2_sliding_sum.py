def slide():
    input_array: list = [2, 1, 5, 1, 3, 2]
    max_sum = -1
    slide_size = 3
    sliding_sum = 0
    for idx in range(len(input_array)):
        if idx < slide_size:
            sliding_sum += input_array[idx]
        else:
            if max_sum < sliding_sum:
                max_sum = sliding_sum
            sliding_sum += input_array[idx] - input_array[idx - slide_size]
    return max_sum


if __name__ == '__main__':
    print(slide())
    pass
