import sys
input = sys.stdin.readline
import heapq

n = int(input())
nums = list(map(int, input().split()))

# unique_nums = dict(enumerate(sorted(set(nums))))
# key_value_reverse = {v:k for k,v in unique_nums.items()}
sorted_nums = sorted(set(nums))
key_value_reverse = dict(zip(sorted_nums, range(len(sorted_nums))))

for i in nums:
    print(key_value_reverse[i], end=" ")