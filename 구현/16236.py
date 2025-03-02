import sys
from collections import deque
# import heapq
input = sys.stdin.readline

n = int(input())

map = [[] for _ in range(n)]
start = []
size = 2
size_stack = 0
for i in range(n):
    now = input().split()
    for j in range(n):
        map[i].append(int(now[j]))
        if now[j] == '9':
            start = [i, j]


vec = [[0, 1], [-1, 0], [1, 0], [0, -1]]

def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    visited = [[False] * n for _ in range(n)]
    feed_list = []
    min_dist = 999

    while queue:
        now_i, now_j = queue.popleft()
        # print("pop", now_i, now_j)

        for k in range(4):
            di, dj = now_i + vec[k][0], now_j + vec[k][1]
            # print(di, dj)
            if  (0 <= di < n) and (0 <= dj < n):
                if not visited[di][dj]:
                    queue.append([di, dj])
                    visited[di][dj] = True

                    feed_size = map[di][dj]
                    if feed_size != 0 and feed_size != 9:
                        dist = abs(i - di) + abs(j - dj)
                        min_dist = min(min_dist, dist)
                        # heapq.heappush(feed_list, [dist, feed_size, di, dj])
                        feed_list.append([dist, feed_size, di, dj])
    return feed_list, min_dist

def get_min_list_from_feed_list(min_dist, sorted_list):
    global size

    min_list = []
    for feed in sorted_list:
        # print(feed)
        if feed[1] <= size:
            if feed[0] == min_dist:
                min_list.append(feed)
            elif feed[0] > min_dist:
                if len(min_list) == 0:
                    min_dist += 1
                    min_list.append(feed)
                else:
                    return min_list
    return min_list

asw = 0
while True:
    feed_list, min_dist = bfs(start[0], start[1])

    # 먹을 것 없으면 종료
    if len(feed_list) == 0:
        print(0)
        break

    # 사이즈업
    if size_stack == size:
        size += 1
        size_stack = 0

    sorted_list = sorted(feed_list, key=lambda x: x[0])
    # print(min_dist, sorted_list)

    # dist 기준 하나씩 꺼내면서 dist 최소면서 size 현재보다 작은 것들만 : 만약 최소 dist에 없으면 하나씩 올려가면서 확인
    min_list = get_min_list_from_feed_list(min_dist, sorted_list)
    print("start: ", start)
    print("size: ", size)
    print("min_list: ", min_list)

    # 먹기
    feed = []
    if len(min_list) > 1:
        resorted_list = sorted(min_list, key=lambda x:(x[2], x[3]))
        print("resorted_list", resorted_list)
        feed = resorted_list[0]
    elif len(min_list) == 1:
        feed = min_list[0]
    print('feed: ', feed)

    map[start[0]][start[1]] = 0
    map[feed[2]][feed[3]] = 9
    start = [feed[2], feed[3]]
    size_stack += 1
    
    print(asw, feed[0])
    asw = asw + feed[0]

    for i in map:
        print(i)
print(asw)