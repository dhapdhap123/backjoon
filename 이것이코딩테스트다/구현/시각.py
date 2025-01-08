n = int(input())
print(15 * 15 * n)

k = 3600 - 45 * 45
for i in range(n):
    if (i == 3):
        k += 3600
    else:
        k += 3600 - 45 * 45
print(k)