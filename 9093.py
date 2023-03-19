a = int(input())
b = []
while a > 0:
    a -= 1
    b.append(str(input()))
c = []
# b = ['abc def', 'ab cd ef']
for i in b:
    # i = ['abc', 'def']
    for j in i.split():
        # j = 'abc'
        c.append(''.join(list(reversed(j))))
    print(' '.join(c))
    c = []
