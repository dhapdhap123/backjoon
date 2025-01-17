# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x - 1) + fibo(x - 2)
# print(fibo(4))

# 탑다운 방식
# d = [0] * 100
# def fibo(x):
#     print('f(' + str(x) + ")", end=' ')
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x - 1) + fibo(x - 2)
#     return d[x]

# print(fibo(6))

# 반복문
d = [0] * 100
d[1] = 1
d[2] = 1
n = 6

for i in range(3, n+1):
    print('f(' + str(i) + ")", end=' ')
    d[i] = d[i - 1] + d[i - 1]
print(d[n])