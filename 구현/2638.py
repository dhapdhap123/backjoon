import sys
input = sys.stdin.readline
from collections import deque

def dfs():
    queue = deque([(0, 0)])
    melt = deque([])

    while queue:
        x, y = queue.popleft()
        print(x, y)
        for k in visited:
            print(k)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if grid[x][y] == 0 and grid[nx][ny] == 1:
                    new_cnt = visited[nx][ny] + 1

                    if new_cnt >= 2:
                        melt.append((nx, ny))
                    else:
                        grid[nx][ny] = new_cnt
                if grid[nx][ny] == 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
    for x, y in melt:
        grid[x][y] = 0  # 공기와 닿은 치즈를 한 번에 녹임
    return len(melt)

N, M = list(map(int, input().split()))
grid = []
cnt = 0

for i in range(N):
    grid.append(list(map(int, input().split())))
    cnt += sum(grid[i])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while True:
    visited = [[0] * M for _ in range(N)]
    melt_num = dfs()
    cnt -= melt_num
    if cnt == 0:
        print(time)
        break
    
    time += 1