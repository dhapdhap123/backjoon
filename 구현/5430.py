import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

# 함수로 구현
# def get_result():
#     for i in range(len(orders)):
#         if orders[i] == 'R':
#             ord = -1 * ord
#         if orders[i] == 'D':
#             if len(nums) == 0:
#                 return "error"            
            
#             if ord == 1:
#                 nums.popleft()
#             elif ord == -1:
#                 nums.pop()
#     if ord == -1:
#         nums.reverse()
#     return f"[{','.join(list(nums))}]"

# for i in range(T):
#     ord = 1
#     orders = list(input().rstrip())
#     n = int(input())
#     str = input().rstrip()[1: -1]
#     nums = []
#     if str:
#         nums = deque(str.split(','))
#     result = get_result()
#     print(result)

# for 문으로 구현
import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    ord = 1
    orders = list(input().rstrip())
    n = int(input())
    str = input().rstrip()[1:-1]
    nums = deque(str.split(',')) if str else deque()

    for command in orders:
        if command == 'R':
            ord *= -1
        elif command == 'D':
            if not nums:
                print("error")
                break
            if ord == 1:
                nums.popleft()
            else:
                nums.pop()
    else:
        if ord == -1:
            nums.reverse()
        print(f"[{','.join(nums)}]")