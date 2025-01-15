import sys
n, m = list(map(int, sys.stdin.readline().rstrip().split()))
array = list(map(int, sys.stdin.readline().rstrip().split()))

# 내 답 : 출력 초과
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
    
#     pivot = array[0]
#     tail = array[1:]

#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x > pivot]

#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# sorted_array = quick_sort(array)

# num_array = []
# last_num = -99999
# sum = 0
# for i in range(sorted_array[-1], 0, -1):
#     if sum >= m:
#         print(i)
#         break
    
#     if last_num == -99999:
#         last_num = sorted_array.pop()
#         num_array.append(last_num)
#         last_num = sorted_array.pop()
#     elif last_num == i:
#         num_array.append(last_num)
#         if sorted_array:
#             last_num = sorted_array.pop()
    
#     sum += len(num_array)

start = 0
end = max(array)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
            
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)