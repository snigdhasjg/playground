from typing import List


def sequentialDigits(low: int, high: int) -> List[int]:
    low_length, high_length = len(str(low)), len(str(high)) + 1
    final = list()
    for i in range(low_length, high_length):
        for j in range(1, 10 - i + 1):
            num = j
            for k in range(1, i):
                num = (num * 10) + j + k
            if low <= num <= high:
                final.append(num)
    return final


def uniquePathsIII(grid: List[List[int]]) -> int:
    pass


def findMaximumXOR(self, nums: List[int]) -> int:
    pass


def lengthOfLastWord(s: str) -> int:
    split = list(filter(lambda word: word != '', s.split(' ')))
    return 0 if len(split) == 0 else len(split[-1])


if __name__ == '__main__':
    length = lengthOfLastWord('a')
    print(length)
