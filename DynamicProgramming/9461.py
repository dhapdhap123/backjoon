import sys
input = sys.stdin.readline
n = int(input().rstrip())

nums = []
for i in range(n):
    nums.append(int(input().rstrip()))
max_num = max(nums)

dp = [1] * (max_num + 1)
for i in range(1, max_num + 1):
    if i == 1 or i == 2 or i == 3:
        dp[i] = 1
    elif i == 4 or i == 5:
        dp[i] = 2
    else:
        dp[i] = dp[i - 1] + dp[i - 5]

for i in nums:
    print(dp[i])