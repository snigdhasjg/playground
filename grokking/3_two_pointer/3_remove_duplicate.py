def remove_duplicate(nums: list):
    output = []
    len_input_array = len(nums)
    first_pointer = 0
    second_pointer = 1
    last_duplicate = None
    while True:
        if nums[first_pointer] != last_duplicate:
            output.append(nums[first_pointer])
            last_duplicate = nums[first_pointer]
        if second_pointer >= len_input_array:
            break
        if nums[first_pointer] == nums[second_pointer]:
            first_pointer = second_pointer + 1
            second_pointer = first_pointer + 1
        else:
            first_pointer += 1
            second_pointer += 1

    return output


if __name__ == '__main__':
    input_array = [2, 3, 3, 3, 4]
    print(remove_duplicate(input_array))
