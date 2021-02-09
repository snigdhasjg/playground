from typing import List, Any


def find_permutation(input_array: List[Any]):
    output: List[List[Any]] = [[]]

    for each in input_array:
        len_output = len(output)
        for i in range(len_output):
            subset = output.pop(0)
            for j in range(len(subset) + 1):
                subset_copy = subset[:]
                subset_copy.insert(j, each)
                output.append(subset_copy)

    return output


if __name__ == '__main__':
    print(find_permutation([1, 2, 3]))
