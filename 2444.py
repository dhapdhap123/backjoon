a = int(input())
b = []
for i in range(1, a*2):
    if i <= a:
        b.append(' ' * (a - i) + '*' * (i*2 - 1))
    else:
        b.append(b[2 * a - i - 1])
for i in range(len(b)):
    print(b[i])