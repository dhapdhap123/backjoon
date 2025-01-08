# 내 정답
# n, m = map(int, input().split())
# y, x, direction = map(int, input().split())

# map_list = []
# for i in range(n):
#     map_list.append(list(map(int, input().split())))

# map_list[x][y] = 1

# def rotate():
#     global direction
#     if direction == 0:
#         direction = 3
#     else:
#         direction -= 1
# def move():
#     global turn_time
#     global asw
#     asw += 1
#     turn_time = 0
#     map_list[x][y] = 1

# asw = 1
# turn_time = 0
# while True:
#     rotate()
#     turn_time += 1
#     if (direction == 0):
#         if (y > 0 and map_list[x][y - 1] != 1):
#             y -= 1
#             move()
#     elif (direction == 1):
#         if (x < n and map_list[x + 1][y] != 1):
#             x += 1
#             move()
#     elif (direction == 2):
#         if (y < n and map_list[x][y + 1] != 1):
#             y += 1
#             move()
#     elif (direction == 3):
#         if (x > 0 and map_list[x - 1][y] != 1):
#             x -= 1
#             move()
    
#     if (turn_time == 4):
#         if (direction == 0):
#             if (y > 0 and map_list[x][y + 1] != 1):
#                 move()
#         elif (direction == 1):
#             if (x < n and map_list[x - 1][y] != 1):
#                 move()
#         elif (direction == 2):
#             if (y < n and map_list[x][y - 1] != 1):
#                 move()
#         elif (direction == 3):
#             if (x > 0 and map_list[x + 1][y] != 1):
#                 move()
#         break
# print(asw)

# 예시 답, 연습
n, m = map(int, input().split())
x, y, direction = map(int, input().split())

d = [[0] * m for _ in range(n)]
d[x][y] = 1

map_list = []
for i in range(n):
    map_list.append(list(map(int, input().split())))

def rotate():
    global direction
    if direction == 0:
        direction = 3
    else:
        direction -= 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_time = 0
while True:
    rotate()
    nx = x + dx[direction]
    ny = x + dy[direction]

    if d[nx][ny] == 0 and map_list[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time ==  4:
        nx = x - dx[direction]
        ny = x - dy[direction]
        if map_list[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)