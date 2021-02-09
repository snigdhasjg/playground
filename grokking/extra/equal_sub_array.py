def find_equal_partitions(nums: list) -> bool:
    total_sum = sum(nums)
    if total_sum & 1 == 1:
        return False
    half_sum = total_sum / 2

    def _find_equal_partitions(_idx: int = 0, _sum_left: int = half_sum) -> bool:
        if len(nums) == _idx:
            return _sum_left == 0
        elif _sum_left == 0:
            return True
        elif _sum_left < 0:
            return False

        return \
            _find_equal_partitions(_idx + 1, _sum_left - nums[_idx]) \
            or \
            _find_equal_partitions(_idx + 1, _sum_left)

    return _find_equal_partitions()


if __name__ == '__main__':
    print(find_equal_partitions([1, 2, 3, 4]))
