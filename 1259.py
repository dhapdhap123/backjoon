a = input()
b = []

for i in range(len(a)-1, -1, -1):
    b.append(a[i])

c = ('').join(b)
if (a == c):
    print('yes')
else:
    print('no')