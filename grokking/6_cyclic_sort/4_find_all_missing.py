def sort_and_find_missing(param):
    for i in range(len(param)):
        while param[i] != i + 1:
            num_idx = param[i] - 1
            if param[num_idx] == param[i]:
                break
            param[i], param[num_idx] = param[num_idx], param[i]

    missing_numbers = []
    for i in range(len(param)):
        if param[i] != i + 1:
            missing_numbers.append(i + 1)
    return param, missing_numbers


if __name__ == '__main__':
    print(sort_and_find_missing([2, 4, 1, 2]))
