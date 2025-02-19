import sys
input = sys.stdin.readline

# 노드 수
n = int(input()) 
# 간선 수
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
dfs(graph, 1, visited)

count = 0
for i in range(2, n + 1):
    if visited[i] == True:
        count += 1
print(count)
