n = int(input())
k = list(map(int, input().split()))

d = [0] * 1001

d[1] = k[1]
d[2] = max(k[1], k[2])


for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + k[i])

print(d[n - 1])