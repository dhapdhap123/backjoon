base = [1, 1, 2, 2, 2, 8]

a = input().split(' ')
a = [int(a[i]) for i in range(len(a))]

diff = []
for i in range(len(a)):
    diff.append(str(base[i] - a[i]))
print(' '.join(diff))