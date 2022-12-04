def process_input():
    def create_range_group(line_input):
        groups = line_input.split(',')

        def create_range_list(input_group):
            input_group_split = input_group.split('-')
            return int(input_group_split[0]), int(input_group_split[1])

        return create_range_list(groups[0]), create_range_list(groups[1])

    def check_overlap(group_set):
        def __check(group_1, group_2):
            return group_1[0] <= group_2[0] and \
                   group_1[1] >= group_2[1] or \
                   group_2[0] <= group_1[1] <= group_2[1]  # this line is for part 2, comment to get answer for part 1

        return __check(group_set[0], group_set[1]) or __check(group_set[1], group_set[0])

    with open('input/day4.txt') as file:
        count = 0
        for line in file:
            if check_overlap(create_range_group(line)):
                count += 1
        return count


if __name__ == '__main__':
    print(process_input())
