n = int(input())

dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(1, n + 1):
    if i == 1:
        dp[1] = 1
    if i == 2:
        dp[2] = 2
    else:
        dp[i] = dp[i - 3] + 1

if dp[n] % 2 == 0:
    print("SK")
else:
    print("CY")