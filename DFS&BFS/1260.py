n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort()

for k, j in edges:
    graph[k].append(j)
    graph[j].append(k)

for g in graph:
    g.sort()

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

dfs_asw = []
bfs_asw = []
# 깊은 것부터. 재귀로
def dfs(graph, v, visited):
    # if visited[v] == False:
    visited[v] = True
    dfs_asw.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 가까운 것부터
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    
    # if visited[start] == False:
    visited[start] = True

    while queue:
        v = queue.popleft()
        bfs_asw.append(v)

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, v, visited_dfs)
bfs(graph, v, visited_bfs)
print(" ".join(map(str, dfs_asw)))
print(" ".join(map(str, bfs_asw)))