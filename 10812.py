(n, m) = input().split(' ')

a = [i for i in range(1, int(n) + 1)]

info = []
for i in range(int(m)):
    info.append(input().split(' '))

# info에서 하나씩 빼서
for i in info:
    # start, end로 a slicing하기.
    start = int(i[0])
    end = int(i[1])
    mid = int(i[2])

    a[start-1:end] = a[mid-1:end]+a[start-1:mid-1]
print(' '.join(map(str, a)))
