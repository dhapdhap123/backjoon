import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10000)

n = int(input().rstrip())
nums_list = list(map(int, input().split()))
m = int(input().rstrip())
searched_list = list(map(int, input().split()))

sorted_nums = sorted(nums_list)

# 재귀 함수 구현
def bs(start, end, target):
    mid = (start + end) // 2

    if start > end:
        return False

    if sorted_nums[mid] == target:
        return True
    elif sorted_nums[mid] < target:
        start = mid + 1
    elif sorted_nums[mid] > target:
        end = mid - 1

    return bs(start, end, target)

# while문 구현
# def bs(start, end, target):
#     while start <= end:
#         mid = (start + end) // 2

#         if sorted_nums[mid] == target:
#             return True
#         elif sorted_nums[mid] < target:
#             start = mid + 1
#         elif sorted_nums[mid] > target:
#             end = mid - 1
#     return False

for i in searched_list:
    if bs(0, n - 1, i):
        print(1)
    else:
        print(0)