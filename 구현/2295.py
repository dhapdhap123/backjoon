import sys
input = sys.stdin.readline

N = int(input())

num_li = []
for i in range(N):
    num_li.append(int(input()))
num_set = set(num_li)
sum_set = set({})

num_li = sorted(num_li, reverse=True)

# 두 수 더한 숫자들 집합

combinations = []

for x in range(N):
    for y in range(N):
        sum_set.add(num_li[x] + num_li[y])
def solution():
    for x in range(N-1):
        for y in range(x+1, N):
            dif = num_li[x]-num_li[y]
            if (dif) in sum_set:
                print(num_li[x])
                return
solution()
