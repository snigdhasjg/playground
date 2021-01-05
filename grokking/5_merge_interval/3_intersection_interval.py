def intersect(left: list, right: list) -> list:
    return [max(left[0], right[0]), min(left[1], right[1])]


def find_intersection(arr1: list, arr2: list):
    idx_arr1 = 0
    idx_arr2 = 0
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    output = []
    while idx_arr1 < len_arr1 and idx_arr2 < len_arr2:
        intersected = intersect(arr1[idx_arr1], arr2[idx_arr2])
        if intersected[0] <= intersected[1]:
            output.append(intersected)
        if arr1[idx_arr1][1] > arr2[idx_arr2][1]:
            idx_arr2 += 1
        else:
            idx_arr1 += 1
    return output


#
# def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
#     i, j = 0, 0
#     res = []
#     while i < len(A) and j < len(B):
#         lo = max(A[i][0], B[j][0])
#         hi = min(A[i][1], B[j][1])
#         if lo <= hi:
#             res.append([lo,hi])
#         if A[i][1] < B[j][1]:
#             i += 1
#         else:
#             j += 1
#     return res


if __name__ == '__main__':
    print(find_intersection(arr1=[[0, 2], [5, 10], [13, 23], [24, 25]], arr2=[[1, 5], [8, 12], [15, 24], [25, 26]]))

# 4 1 6 8 2
#  1<=n<=10

# 1 1 0 1 0 1 0 1 0 0
