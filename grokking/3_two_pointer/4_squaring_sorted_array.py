def squaring_in_order(nums: list):
    length = len(nums)
    output = [None] * length
    left_pointer = 0
    right_pointer = length - 1
    out_index = length - 1
    while True:
        if left_pointer == right_pointer:
            output[out_index] = nums[left_pointer] ** 2
            break
        if left_pointer > right_pointer:
            break
        left_square = nums[left_pointer] ** 2
        right_square = nums[right_pointer] ** 2
        if left_square > right_square:
            left_pointer, right_pointer = left_pointer + 1, right_pointer
            output[out_index] = left_square
            out_index -= 1
        else:
            left_pointer, right_pointer = left_pointer, right_pointer - 1
            output[out_index] = right_square
            out_index -= 1

    return output


if __name__ == '__main__':
    input_array = [-2, -1, 0, 2, 3]
    print(squaring_in_order(input_array))
