import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
S = [[0] * (N) for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    S[i] = row

starts = []
links = []
INF = 1e9
min_dif = INF

def dfs(idx, combi, max_len, visited):
    global min_dif
    visited[idx] = True

    if len(combi) == max_len:
        start = combi
        link = list(filter(lambda x: x not in combi, range(N)))

        A, B = 0, 0
        for i in range((N // 2) - 1):
            for j in range(i + 1, N // 2):
                A += S[start[i]][start[j]] + S[start[j]][start[i]]
                B += S[link[i]][link[j]] + S[link[j]][link[i]]
        min_dif = min(min_dif, abs(A - B))

        new_combi = combi[:]
        new_combi.pop()
        dfs(idx, new_combi, max_len, visited)
    if max_len > len(combi) + N - idx:
        return
    next_idx = idx + 1
    if next_idx < (N) and visited[next_idx] == False:
        return dfs(next_idx, combi + [next_idx], max_len, visited)

# starts 추출
for i in range(N):
    combi = [i]
    max_len = N // 2
    visited = [False] * (N)
    dfs(i, combi, max_len, visited)

print(min_dif)