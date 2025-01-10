# 풀이 1 : min 함수 사용
# n, m = map(int, input().split())

# result = 0
# for i in range(n):
#     data = list(map(int, input().split(' ')))
#     min_value = min(data)

#     result = max(result, min_value)
# print(result)

# 풀이 2 : 이중 반복문
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split(' ')))
    
    min_value = 10001 # 최대 숫자가 10000임
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)