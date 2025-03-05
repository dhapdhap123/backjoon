import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

def get_result(ord):
    for i in range(len(orders)):
        if orders[i] == 'R':
            ord = -1 * ord
        if orders[i] == 'D':
            if len(nums) == 0:
                return "error"            
            
            if ord == 1:
                nums.popleft()
            elif ord == -1:
                nums.pop()
    if ord == -1:
        nums.reverse()
    return f"[{','.join(list(nums))}]"

for i in range(T):
    ord = 1
    orders = list(input().rstrip())
    n = int(input())
    str = input().rstrip()[1: -1]
    nums = []
    if str:
        nums = deque(str.split(','))
    result = get_result(ord)
    print(result)