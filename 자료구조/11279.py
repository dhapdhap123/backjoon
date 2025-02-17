import heapq

import sys
input = sys.stdin.readline
n = int(input())

heap = []
for i in range(n):
  num = int(input())
  if num == 0:
    if len(heap) > 0:
      print(-1 * heapq.heappop(heap))
    else:
      print(0)
  else:
    heapq.heappush(heap, -1 * num)