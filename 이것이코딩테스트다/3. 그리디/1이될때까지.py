n, k = map(int, input().split())
asw = 0
while n > 1:
    if (n % k != 0):
        n -= 1
    else:
        n /= k
    asw += 1
print(asw)