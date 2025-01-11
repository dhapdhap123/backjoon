# 재귀 함수
# found_num = int(input())
array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# def binary_search(array, found_num, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == found_num:
#         return mid
#     elif array[mid] > found_num:
#         return binary_search(array, found_num, start, mid - 1)
#     elif array[mid] < found_num:
#         return binary_search(array, found_num, mid + 1, end)
    
# print(binary_search(array, 16, 0, 9))

# 반복문
def binary_search(array, found_num, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == found_num:
            return mid
        elif array[mid] > found_num:
            end = mid - 1
        else: start = mid + 1
    return None

print(binary_search(array, 4, 0, 9))