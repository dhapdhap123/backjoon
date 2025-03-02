import sys
input = sys.stdin.readline

K, N = list(map(int, input().split()))
lans = []
for _ in range(K):
    lans.append(int(input().rstrip()))

# asw = []

def cut_lans(lans, length):
    sum = 0

    if length == 0:
        return sum

    for i in lans:
        if i >= length:
            sum += (i // length)
    return sum

def binary_search(start, end, N):
    asw = 0

    while start <= end:
        mid = (start + end) // 2

        sum = cut_lans(lans, mid)
        # if sum == N:
        #     return mid
        if sum >= N:
            start = mid + 1
            asw = max(asw, mid)
        else:
            end = mid - 1
    if asw:
        return asw
    else:
        return 1

result = binary_search(0, max(lans), N)
# if asw:
#     print(max(max(asw), result))
# else:
print(result)


# 최적화
start, end = 1, max(lans)
while start <= end:
    mid = (start + end) // 2
    print(mid)

    line_cnt = 0

    for lan in lans:
        line_cnt += lan // mid

    if line_cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)