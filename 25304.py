x = int(input())
n = int(input())
sum = 0
while n > 0:
    a, b = map(int, input().split())
    sum += (a * b)
    n -= 1

if x == sum:
    print("Yes")
else:
    print("No")