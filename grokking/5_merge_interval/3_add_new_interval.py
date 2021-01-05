def merge(left: list, right: list) -> list:
    return [min(left[0], right[0]), max(left[1], right[1])]


def check_if_mergeable(left: list, right: list) -> bool:
    # [1,4] [2,6]
    # [2,6] [1,4]
    # [1,2] [4,5]
    # [4,5] [1,2]
    # [1,4] [2,3]
    # [2,3] [1,4]
    # [1,4] [1,4]
    # [4,5] [1,4]
    return left[1] >= right[0] and right[1] >= left[0]


def merge_input_sorted(sorted_array: list):
    output = []
    start_pointer = 0
    end_pointer = start_pointer + 1
    last_merged: list = None
    length_of_array = len(sorted_array)
    while end_pointer < length_of_array:
        if last_merged:
            if check_if_mergeable(last_merged, sorted_array[end_pointer]):
                last_merged = merge(last_merged, sorted_array[end_pointer])
                end_pointer += 1
            else:
                output.append(last_merged)
                last_merged = None
                start_pointer = end_pointer
                end_pointer = start_pointer + 1
        else:
            if check_if_mergeable(sorted_array[start_pointer], sorted_array[end_pointer]):
                last_merged = merge(sorted_array[start_pointer], sorted_array[end_pointer])
                end_pointer += 1
            else:
                output.append(sorted_array[start_pointer])
                start_pointer = end_pointer
                end_pointer = start_pointer + 1

    if last_merged:
        output.append(last_merged)
    elif start_pointer < length_of_array:
        output.append(sorted_array[start_pointer])

    return output


def merge_inputs(input_array: list, new_interval: list):
    for index, value in enumerate(input_array):
        if value[0] > new_interval[0]:
            input_array.insert(index, new_interval)
            break
    print(input_array)
    return merge_input_sorted(input_array)


if __name__ == '__main__':
    print(merge_inputs([[1, 3], [5, 7], [8, 12]], [4, 6]))
