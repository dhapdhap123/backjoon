pos = input()
x_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x, y = int(x_list.index(pos[0]) + 1), int(pos[1])

asw = 0
move_list = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
for i in move_list:
    next_x = x + i[0]
    next_y = y + i[1]

    if (next_x >= 1 and next_y <= 8 and next_x <= 8 and next_y >= 1):
        asw += 1
print(asw)