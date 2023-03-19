n = int(input())

for _ in range(n):
    mean = 0
    nums = 0
    k = list(map(int, input().split()))
    mean = sum(k[1:])/k[0]
    
    for j in range(1, len(k)):
        if (k[j] > mean):
            nums += 1
    t = nums / k[0] * 100
    print("{:.3f}%".format(t))