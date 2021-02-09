from typing import List, Any


def find_all_subset(input_array: List[Any]):
    output: List[List[Any]] = [[]]

    for each in input_array:
        len_output = len(output)
        for i in range(len_output):
            new_out = output[i][:]
            new_out.append(each)
            output.append(new_out)

    return output


if __name__ == '__main__':
    print(find_all_subset([1, 2, 3]))
