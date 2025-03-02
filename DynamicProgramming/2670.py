import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = [1]
for i in range(n):
    nums.append(float(input().rstrip()))

for i in range(1, n):
    nums[i] = max(nums[i], nums[i] * nums[i - 1])    
print("%0.3f" % max(nums))