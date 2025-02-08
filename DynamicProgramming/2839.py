import sys
input = sys.stdin.readline

n = int(input())


# dp 이용
# dp = [-1] * 5001
# dp[3] = 1
# dp[5] = 1

# if n <= 5:
#   print(dp[n])
# else:
#   for i in range(6, n + 1):
#     if i % 3 == 0:
#       dp[i] = i // 3
#     elif i % 5 == 0:
#       dp[i] = i // 5
#     elif dp[i - 5] == -1 and dp[i - 3] == -1:
#       dp[i] = -1
#     else:
#       if dp[i - 5] >= dp[i - 3] or dp[i - 5] == -1:
#         dp[i] = dp[i - 3] + 1
#       elif dp[i - 3] >= dp[i - 5] or dp[i - 3] == -1:
#         dp[i] = dp[i - 5] + 1
#     print(i, dp[i])
#   print(dp[n])

# while 이용
count = 0
while n >= 0:
  if n % 5 == 0:
    count += int(n // 5)
    print(count)
    break

  n -= 3
  count += 1
else:
  print(-1)