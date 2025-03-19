import sys
input = sys.stdin.readline
from collections import deque

N, M = list(map(int, input().split()))
maps = list(map(int, input().split()))
asw = 0
for i in range(1, M - 1):
    left_max = max(maps[:i])
    right_max = max(maps[i:])

    lower = min(left_max, right_max)

    if maps[i] < lower:
        asw += lower - maps[i]
print(asw)