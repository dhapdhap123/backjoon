import sys
input = sys.stdin.readline
from itertools import permutations
import copy
from collections import deque

N, M = list(map(int, input().split()))
grid = [[] for _ in range(N)]

zero_list = []
two_list = []
for i in range(N):
    now = list(map(int, input().split()))
    for j in range(len(now)):
        if now[j] == 0:
            zero_list.append([i, j])
        elif now[j] == 2:
            two_list.append([i, j])
        grid[i].append(now[j])
# 조합 구하기
permutation = list(permutations(zero_list, 3))

# len(zero_list)에서 변한 개수 빼주면 안전개수
vec = [[1, 0], [-1, 0], [0, 1], [0, -1]]
# def dfs(i, j, grid):
#     global cnt

#     if grid[i][j] == 0:
#         grid[i][j] = 2
#         cnt += 1

#     for v in range(4):
#         new_i, new_j = i + vec[v][0], j + vec[v][1]
#         if 0 <= new_i < N and 0 <= new_j < M:
#             if grid[new_i][new_j] == 0:
#                 dfs(new_i, new_j, grid)
def bfs(grid):
    global cnt
    while dq:
        x, y = dq.popleft()

        for v in range(4):
            new_x, new_y = x + vec[v][0], y + vec[v][1]
            if 0 <= new_x < N and 0 <= new_y < M:
                if grid[new_x][new_y] == 0:
                    grid[new_x][new_y] = 2
                    cnt += 1
                    dq.append([new_x, new_y])

max_zero = 0
for p in permutation:
    new_grid = copy.deepcopy(grid)
    cnt = 0

    # print(two[0], two[1], cnt)
    for i in p:
        new_grid[i[0]][i[1]] = 1

    dq = deque(two_list)
    bfs(new_grid)
    zero_num = len(zero_list) - 3 - cnt
    if max_zero < zero_num:
        max_zero = zero_num

print(max_zero)
