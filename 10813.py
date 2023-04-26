n, m = map(int, input().split())
list = [i + 1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    k = list[i - 1]
    list[i - 1] = list[j - 1]
    list[j - 1] = k
print(list)