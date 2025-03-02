import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = list(map(int, input().split()))

stores = []
homes = []

for i in range(N):
    now = list(map(int, input().split()))
    for j in N:
        if now[j] == 1:
            homes.append([i, j])
        elif now[j] == 2:
            stores.append([i, j])
