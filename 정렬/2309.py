import sys
input = sys.stdin.readline

list = [int(input()) for _ in range(9)]
sorted_list = sorted(list)

total = sum(sorted_list)
two_sum = total - 100
num_1 = 0
num_2 = 0
for i in range(len(sorted_list)):
    for j in range(i + 1, len(sorted_list)):
        if sorted_list[i] + sorted_list[j] == two_sum:
            num_1 = sorted_list[i]
            num_2 = sorted_list[j]
            break
sorted_list.remove(num_1)
sorted_list.remove(num_2)
for i in sorted_list:
    print(i)
