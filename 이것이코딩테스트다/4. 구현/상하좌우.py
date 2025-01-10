n = int(input())
order = list(input().split())

now_spot = [1, 1]
for i in order:
    if i == "R":
        if now_spot[1] < n:
            now_spot[1] += 1
    elif i == "L":
        if now_spot[1] > 1:
            now_spot[1] -= 1
    if i == "U":
        if now_spot[0] > 1:
            now_spot[0] -= 1
    elif i == "D":
        if now_spot[0] < n:
            now_spot[0] += 1
print(" ".join(map(str, now_spot)))