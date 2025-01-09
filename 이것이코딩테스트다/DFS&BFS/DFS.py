# DFS(Depth-First Search)는 깊이 우선 탐색. 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

# 그래프는 프로그래밍에서 두 가지 방식으로 표현 가능
# 1. 인접 행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식

# INF = 999999999
# graph = [
#     [0, 7, 5],
#     [7, 0, INF],
#     [5, INF, 0]
# ]
# print(graph)

# 2. 인접 리스트 : 리스트로 그래프의 연결 관계를 표현하는 방식
# graph = [[] for _ in range(3)]

# graph[0].append((1, 7))
# graph[0].append((2, 5))

# graph[1].append((0, 7))

# graph[2].append((0, 5))
# print(graph)
visited = [False] * 9
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

dfs(graph, 1, visited)