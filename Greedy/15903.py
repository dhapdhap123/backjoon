import sys
import heapq
input = sys.stdin.readline


heap = []
n, m = list(map(int, input().split()))
[heapq.heappush(heap, i) for i in list(map(int, input().split()))]

for i in range(m):
  x = heapq.heappop(heap)
  y = heapq.heappop(heap)
  sum = x + y
  heapq.heappush(heap, sum)
  heapq.heappush(heap, sum)

sum = 0
for i in heap:
  sum += i
print(sum)