import sys
input = sys.stdin.readline
import heapq

pq = []
N, H, T = list(map(int, input().split()))
for i in range(N):
    heapq.heappush(pq, -1 * int(input()))
cnt = 0
for i in range(T):
    if -pq[0] == 1 or -pq[0] < H:
        break
    else:
        heapq.heapreplace(pq, -(-pq[0] // 2))
        cnt += 1

if -pq[0] >= H:
    print('NO', -pq[0], sep='\n')
else:
    print('YES', cnt, sep='\n')