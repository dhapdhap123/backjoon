import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = 0
right = 0
long = 0
counter = dict({
    arr[0]: 1
})

while left < N and right < N:
    if counter[arr[right]] > K:
        while counter[arr[right]] > K:
            counter[arr[left]] -= 1
            left += 1
    else:
        long = max(long, right - left + 1)
        right += 1
        if right < N:
            if arr[right] in counter:
                counter[arr[right]] += 1
            else:
                counter[arr[right]] = 1
            

print(long)