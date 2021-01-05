def find_missing(param):
    param.append(-1)
    for i in range(len(param)):
        while param[i] != i and param[i] != -1:
            num_idx = param[i]
            param[i], param[num_idx] = param[num_idx], param[i]

    for i in range(len(param)):
        if param[i] == -1:
            return i
    return 0


if __name__ == '__main__':
    print(find_missing([4, 2, 3, 1]))
