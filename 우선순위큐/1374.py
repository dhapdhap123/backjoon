import sys
input = sys.stdin.readline
import heapq

N = int(input())
times = []
for i in range(N):
    times.append(list(map(int, input().split())))
times.sort(key=lambda x: x[1])

pq = []
for i in times:
    if pq:
        if pq[0] <= i[1]:
            heapq.heapreplace(pq, i[2])
        else:
            heapq.heappush(pq, i[2])    
    else:
        # 끝나는 시간 넣기
        heapq.heappush(pq, i[2])
print(len(pq))