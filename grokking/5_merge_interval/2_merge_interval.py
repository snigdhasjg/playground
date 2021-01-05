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


# def merge_inputs(input_array: list):
#     start_pointer = 0
#     end_pointer = start_pointer + 1
#     while True:
#         # print(input_array)
#         length = len(input_array)
#         if start_pointer >= length - 1:
#             break
#         if check_if_mergeable(input_array[start_pointer], input_array[end_pointer]):
#             input_array[start_pointer] = merge(input_array[start_pointer], input_array[end_pointer])
#             input_array.pop(end_pointer)
#             end_pointer = start_pointer + 1
#         else:
#             if end_pointer < length - 1:
#                 end_pointer += 1
#             else:
#                 start_pointer += 1
#                 end_pointer = start_pointer + 1
#     return input_array


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


def merge_inputs(input_array: list):
    sorted_array = sorted(input_array, key=lambda x: x[0])
    merge_input_sorted(sorted_array)


if __name__ == '__main__':
    input_arr = [[1, 2], [2, 6], [7, 8], [9, 10], [10, 11]]
    print(merge_inputs(input_arr))
    print(merge_input_sorted(input_arr))
