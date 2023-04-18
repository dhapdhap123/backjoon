n = int(input())
list = []
while n > 0:
    x, y = map(int, input().split())
    list.append(str(x + y))
    n -= 1
print('\n'.join(list))