"""
We are willing to provide lowest price medicine to the customer.
To achieve this, we started suggesting different substitute medicines having the lowest price to the customer.
Every medicine has a different salt combination.
We store this salt combination information in our system and assign it to an integer score.
We are looking for substitute products having minimal salt difference.
We say a product is a matching substitute only if its integer score has the same number of set bits as the user asked for.
Implement an algorithm that takes the score of the asked product and returns the score for a substitute product.

Example
Binary Representation of 10 is 1010

Numbers with same binary Representations:
12 – 1100   difference with 10  is 2
 3  – 0011   difference with 10  is 7
 6  – 0110   difference with 10  is 4
 9  – 1001   difference with 10  is 1
6   – 0110   difference with 10  is 4

your algorithm should return: 9

I/P: 2 – 10
O/P: 1 – 01
I/O: 7 – 111
O/P: 11 – 1011
I/O:  5 – 101
O/P: 6 – 110
"""


def binary(number) -> str:
    if number <= 1:
        return f'{number}'
    reminder = number % 2
    return f'{int(binary(number // 2))}{reminder}'


def decimal(binary_string):
    pass


def solution(number):
    binary_number_string = list(number)  # 1010
    # total_1s = sum([1 if each_digit == '1' else 0 for each_digit in list(binary_number)])
    # total_len = len(binary_number)
    index_of_one = -1  # 2
    index_of_zero = -1  # 1
    for i in range(len(binary_number_string) - 1, -1, -1):
        if binary_number_string[i] == '0':
            index_of_zero = i
        elif binary_number_string[i] == '1':
            index_of_one = i

        if index_of_one != -1 and index_of_zero != -1:
            break

    if index_of_zero == -1:
        binary_number_string.insert(0, '0')
        index_of_zero = 0
        index_of_one += 1

    binary_number_string[index_of_zero], binary_number_string[index_of_one] = binary_number_string[index_of_one], \
        binary_number_string[index_of_zero]

    return ''.join(binary_number_string)


# if __name__ == '__main__':
#     print(solution('111000'))  # 110100
#     print(solution('1010'))  # 1001
#     print(solution('10111'))  # 11011
#     print(solution('111'))  # 1011
#     print(solution('110011'))  # 110101
#
#     print(binary(11))
#
#     print(solution('101010'))
#
#     print(int('101010', 2), int('101001', 2))

# 111000

if __name__ == '__main__':
    # number = 12
    # print(f'Binary of {number}: {binary(number)}')
    # shifted = number << 2
    # print(f'After shifting {shifted}: {binary(shifted)}')

    number1 = 4
    number2 = 5
    print(f'{number1}: {binary(number1)}, {number2}: {binary(number2)}')
    print(f'{number1 ^ number2}: {binary(number1 ^ number2)}')
