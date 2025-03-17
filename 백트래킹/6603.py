from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    nums = input().rstrip().split()
    if len(nums) == 1:
        break
    k = nums[0]
    s = nums[1:]
    collection = combinations(s, 6)
    for i in collection:
        print(" ".join(i))
    print()