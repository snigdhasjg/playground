from typing import List, Any


def find_all_subset(input_array: List[Any]):
    output: List[List[Any]] = [[]]
    sorted_input = sorted(input_array)
    end_output = 0
    for current_idx in range(len(sorted_input)):
        start_output = 0
        current_number = sorted_input[current_idx]

        if current_idx != 0:
            prev_number = sorted_input[current_idx - 1]
            if current_number == prev_number:
                start_output = end_output

        end_output = len(output)

        for i in range(start_output, end_output):
            new_out = output[i][:]
            new_out.append(current_number)
            output.append(new_out)

    return output


if __name__ == '__main__':
    print(find_all_subset([1, 3, 3, 3]))
