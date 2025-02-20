import sys
input = sys.stdin.readline
from collections import deque
# sys.setrecursionlimit(10000)

n, m = list(map(int, input().split()))
miro = [[] for _ in range(n)]
for i in range(n):
    miro[i] = list(map(int, list(input().rstrip())))

# dfs로 풀면 안됨. 모든 노드 다 방문하지 않아야되는 경우(e.g. 최단거리)엔 bfs가 적합

vec = [[1, 0], [-1, 0], [0, 1], [0, -1]]

visited = [[False] * m for _ in range(n)]
distance = [[1] * m for _ in range(n)]
def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    # visited[y][x] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            dx, dy = vec[i]
            new_x, new_y = x + dx, y + dy

            if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                continue
            if visited[new_y][new_x] == False and miro[new_y][new_x] == 1:
                queue.append([new_x, new_y])
                visited[new_y][new_x] = True
                distance[new_y][new_x] += distance[y][x]
bfs(0, 0)
print(distance[n - 1][m - 1])
# def dfs(x, y, count):
#     # 맵 바깥이나 0일 때
#     print(x, y, count)
#     for i in miro:
#         print(i)
    
#     if x < 0 or x >= m or y < 0 or y >= n or miro[y][x] == 0:
#         return
#     miro[y][x] = 0

#     if (x == m - 1) and (y == n - 1):
#         print('\n')
#         for i in miro:
#             print(i)
#         results.append(count)
#         return
    
    
    
#     dfs(x + 1, y, count + 1)
#     dfs(x - 1, y, count + 1)
#     dfs(x, y + 1, count + 1)
#     dfs(x, y - 1, count + 1)

# dfs(0, 0, 1)
# print(min(results))
