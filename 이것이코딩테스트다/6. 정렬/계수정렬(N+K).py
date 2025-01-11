array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# count = [0] * (max(array) + 1)

# for i in array:
#     count[i] += 1

# for i in range(len(count)):
#     print(" ".join(map(str, count[i] * [i])), end=" ")

# 파이썬 내장 함수 sorted, sort
result = sorted(array)
array.sort()

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]
result = sorted(array, key=setting)
print(result)