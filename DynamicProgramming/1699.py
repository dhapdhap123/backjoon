import sys
input = sys.stdin.readline

n = int(input())


dp = [i for i in range(n + 1)]

# 2부터 n까지
# 1 ~ 2
# 1 ~ 3
# 1 ~ 4
# 1 ~ 5
for i in range(2, n + 1):
    for j in range(1, i + 1):
        square = j * j
        if square > i:
            break

        if dp[i] > dp[i - square] + 1:
            dp[i] = dp[i - square] + 1

print(dp)