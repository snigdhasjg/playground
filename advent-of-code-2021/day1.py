with open('input/day1.txt') as file:
    report = [int(line) for line in file]

import numpy as np

# diff_array = np.diff(report)
# print(len(diff_array[diff_array > 0]))

sliding_sum = np.convolve(report, np.ones(3, dtype=int), 'valid')
diff_array = np.diff(sliding_sum)
print(len(diff_array[diff_array > 0]))

if __name__ == '__main__':
    pass
