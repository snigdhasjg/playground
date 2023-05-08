def find_triplet(nums: list):
    if len(nums) < 3 or min(nums) > 0 or max(nums) < 0:
        return []
    sorted_list = sorted(nums)
    length_of_array = len(sorted_list)
    triplets = []

    def find_sum(index_to_skip: int):
        find_sum_of = -sorted_list[index_to_skip]
        left_index = index_to_skip + 1
        right_index = length_of_array - 1
        while left_index < right_index:
            current_sum = sorted_list[left_index] + sorted_list[right_index]
            if find_sum_of == current_sum:
                triplets.append([-current_sum, sorted_list[left_index], sorted_list[right_index]])
                left_index += 1
                right_index -= 1
                while left_index < right_index and sorted_list[left_index] == sorted_list[left_index - 1]:
                    left_index += 1
                while left_index < right_index and sorted_list[right_index] == sorted_list[right_index + 1]:
                    right_index -= 1
            elif find_sum_of > current_sum:
                left_index += 1
                while left_index < right_index and sorted_list[left_index] == sorted_list[left_index - 1]:
                    left_index += 1
            else:
                right_index -= 1
                while left_index < right_index and sorted_list[right_index] == sorted_list[right_index + 1]:
                    right_index -= 1
        return triplets

    for i in range(length_of_array - 2):
        current_number = sorted_list[i]
        if current_number > 0:
            break
        if i > 0 and current_number == sorted_list[i - 1]:
            continue
        find_sum(i)
    return triplets


if __name__ == '__main__':
    unsorted = [-3, 0, 1, 2, -1, 1, -2]
    print(find_triplet(unsorted))
