import sys
input = sys.stdin.readline
INF = int(1e9) # 무한 의미하는 10억

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 노드에 대한 정보 리스트
graph = [[] for i in range(n + 1)]
# 방문한 적 있는지 체크 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n + 1)

# 간선 정보 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a -> b 비용이 c

    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드 제외 전체 n - 1개 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드 꺼내, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])