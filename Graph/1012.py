import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

t = int(input())
for i in range(t):
    m, n, k = list(map(int, input().split()))
    grid = [[0] * m for _ in range(n)]

    for i in range(k):
        x, y = list(map(int, input().split()))
        grid[y][x] = 1

    def dfs(y, x):
        # 맵 바깥이거나 육지
        if y < 0 or y >= n or x < 0 or x >= m or grid[y][x] == 0:
            return
        
        grid[y][x] = 0
        dfs(y + 1, x)
        dfs(y - 1, x)
        dfs(y, x + 1)
        dfs(y, x - 1)

    count = 0
    for y in range(n):
        for x in range(m):
            if grid[y][x] == 1:
                count += 1
                dfs(y, x)
    print(count)
# bfs
# from collections import deque
# for i in range(t):
#     m, n, k = list(map(int, input().split()))
#     grid = [[0] * (m + 1) for _ in range(n + 1)]

#     for i in range(k):
#         x, y = list(map(int, input().split()))
#         grid[y][x] = 1

    
#     def bfs(y, x):
#         queue = deque([(x, y)])
#         grid[y][x] = 0
#         vec = [[-1, 0], [1, 0], [0, -1], [0, 1]]

#         while queue:
#             x, y = queue.popleft()

#             for i in range(4):
#                 dx, dy = vec[i]
#                 new_x = x + dx
#                 new_y = y + dy
                
#                 if new_y < 0 | new_y >= n | new_x < 0 | new_x >= m:
#                     continue
            
#                 if grid[new_y][new_x] == 1:
#                     queue.append((new_x, new_y))
#                     grid[new_y][new_x] = 0
        
#     count = 0
#     for y in range(n):
#         for x in range(m):
#             if grid[y][x] == 1:
#                 bfs(y, x)
#                 count += 1
#     print(count)