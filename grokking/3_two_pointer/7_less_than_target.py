def find_triplet(nums: list, target: int):
    if len(nums) < 3 or min(nums) > 0 or max(nums) < 0:
        return []
    sorted_list = sorted(nums)
    length_of_array = len(sorted_list)
    count_triplet = 0
    for i in range(length_of_array - 2):
        current_number = sorted_list[i]
        if current_number >= target:
            break
        left_idx = i + 1
        right_idx = length_of_array - 1
        new_target = target - current_number
        while sorted_list[left_idx] < target and left_idx < right_idx:
            if sorted_list[left_idx] + sorted_list[right_idx] >= new_target:
                right_idx -= 1
            else:
                count_triplet += right_idx - left_idx
                left_idx += 1
    return count_triplet


if __name__ == '__main__':
    print(find_triplet([-1, 4, 2, 1, 3], 5))
