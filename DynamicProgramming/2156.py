import sys
input = sys.stdin.readline

N = int(input())
wine_list = [0] * 10000
for i in range(N):
    wine_list[i] = int(input())
dp = [0] * 10000

dp[0] = wine_list[0]
dp[1] = wine_list[0] + wine_list[1]
dp[2] = max(wine_list[2]+wine_list[0], wine_list[2]+wine_list[1], dp[1])
for i in range(3, N):
    dp[i] = max(wine_list[i]+dp[i-2], wine_list[i]+wine_list[i-1]+dp[i-3], dp[i-1])
print(max(dp))