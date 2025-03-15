import sys
input = sys.stdin.readline
import heapq

pq = []
N = int(input())
for i in range(N):
    num = input().rstrip()
    if num == '0':
        if len(pq) > 0:
            print(-1 * heapq.heappop(pq))
        else:
            print(-1)
    else:
        nums = list(map(int, num.split()))
        
        for i in range(1, len(nums)):
            heapq.heappush(pq, -1 * nums[i])