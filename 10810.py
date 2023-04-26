n, m = map(int, input().split())
list = [0 for i in range(n)]
for _ in range(m):
    s, e, num = map(int, input().split())
    list[s - 1 : e] = [num for _ in range(e + 1 - s)]
print(' '.join(map(str, list)))