n = int(input())
array = []
num_list=[]
for _ in range(n):
    x, y = input().split()
    array.append((x, int(y)))
    num_list.append(int(y))

# sort 사용
# array.sort(key=lambda student: student[1])
# for i in array:
#     print(i[0], end=' ')

# 계수 정렬 사용

score_list = [0] * (max(num_list) + 1)
for student in array:
    score = student[1]
    score_list[score] += 1

for idx in range(len(score_list)):
    if score_list[idx]:
        for j in array:
            if j[1] == idx:
                print(j[0], end=" ")