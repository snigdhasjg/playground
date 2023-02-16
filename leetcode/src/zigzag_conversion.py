# https://leetcode.com/problems/zigzag-conversion/

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    placeholders = ['' for _ in range(numRows)]
    max_zig = 2 * numRows - 2

    for i, _s in enumerate(s):
        position_in_zig = i % max_zig
        placeholder_position = position_in_zig if position_in_zig < numRows else -(position_in_zig - numRows + 2)
        placeholders[placeholder_position] += _s

    return ''.join(placeholders)
