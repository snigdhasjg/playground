def get_total_unique_count():
    with open('input/day6.txt') as file:
        group_problem = []
        group = []
        for each_line in file:
            if each_line == '\n':
                if len(group) != 0:
                    group_problem.append(list(set(group)))
                    group = []
            group.extend(list(each_line.strip()))
        group_problem.append(list(set(group)))

    count = 0
    for i in group_problem:
        count += len(i)
    print(count)


def get_intersection_count():
    with open('input/day6.txt') as file:
        group_problem = []
        group = []
        for each_line in file:
            if each_line == '\n':
                if len(group) != 0:
                    group_problem.append(group)
                    group = []
            else:
                group.append(set(each_line.strip()))
        group_problem.append(group)
    return group_problem


def count_unique():
    total_count = 0
    for each_group in get_intersection_count():
        if len(each_group) == 1:
            total_count += len(each_group[0])
        else:
            total_count += count_unique_per_group(each_group)
    return total_count


def count_unique_per_group(each_group):
    set_of_question: set = each_group[0]
    for i in range(1, len(each_group)):
        set_of_question = set_of_question.intersection(each_group[i])
    return len(set_of_question)


if __name__ == '__main__':
    print(count_unique())
