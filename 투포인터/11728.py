import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = 0
j = 0
sorted_list = []
while i != N or j != M:
    if i == N:
        sorted_list.append(B[j])
        j += 1
    elif j == M:
        sorted_list.append(A[i])
        i += 1
    else:
        if A[i] < B[j]:
            sorted_list.append(A[i])
            i += 1
        else:
            sorted_list.append(B[j])
            j += 1
print(*sorted_list)