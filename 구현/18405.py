import sys
input = sys.stdin.readline
from collections import deque

N, K = list(map(int, input().split()))

grid = []
sec_list = [[] for _ in range(K + 1)]
for i in range(N):
    now = list(map(int, input().split()))
    grid.append(now)
    for j in range(N):
        num = now[j]
        if num != 0:
            sec_list[num] = sec_list[num][:] + [[i, j]]
S, X, Y = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(now_sec):
    queue = deque(sec_list[now_sec])
    new_queue = []
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y]
                new_queue.append([nx, ny])
    sec_list[now_sec] = new_queue[:]
now_sec = 0
while True:
    if now_sec > S:
        print(grid[X - 1][Y - 1])
        break
    for i in range(1, K + 1):
        dfs(i)
    now_sec += 1
