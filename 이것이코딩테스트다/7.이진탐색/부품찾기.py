import sys
n = int(sys.stdin.readline().rstrip())
N = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
M = list(map(int, sys.stdin.readline().rstrip().split()))

# def binary_search(array, target, start, end):
#     # if start > end:
#     #     return None
    
#     # mid = (start + end) // 2
#     # if array[mid] == target:
#     #     return mid
#     # elif array[mid] > target:
#     #     return binary_search(array, target, start, mid - 1)
#     # else: return binary_search(array, target, mid + 1, end)
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# N.sort()
# for i in M:
#     result = binary_search(N, i, 0, n)
#     if result == None:
#         print('no', end=" ")
#     else:
#         print('yes', end=" ")

# 계수정렬로 구현
# array = [0] * (1000001)
# for i in N:
#     array[i] += 1

# for j in M:
#     if array[j]:
#         print('yes', end=" ")
#     else:
#         print('no', end=" ")

# 집합으로 구현
for i in M:
    if i in N:
        print('yes')
    else:
        print('no')