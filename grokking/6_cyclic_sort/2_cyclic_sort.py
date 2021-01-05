def sort_in_place(param):
    for i in range(len(param)):
        while param[i] != i + 1:
            num_idx = param[i] - 1
            param[i], param[num_idx] = param[num_idx], param[i]

    return param


if __name__ == '__main__':
    print(sort_in_place([2, 0, 3, 1]))
