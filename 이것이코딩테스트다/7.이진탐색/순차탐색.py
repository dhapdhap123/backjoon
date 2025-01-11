n, target = input().split()
n = int(n)
array = input().split()

idx_list = []
for i in range(n):
    if array[i] == target:
        idx_list.append(i)

print(idx_list)