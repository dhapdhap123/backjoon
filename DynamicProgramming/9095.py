import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    k = int(input())
    dp = [0] * (k + 1)

    for i in range(k):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[k])