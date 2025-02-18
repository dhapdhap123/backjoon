from collections import deque

import sys
input = sys.stdin.readline
n = int(input())
square = [[0] * (n + 1) for i in range(n + 1)]
square[1][1] = 1

# 사과 list에 적용 (-1)
apple_n = int(input())
for i in range(apple_n):
  x, y = list(map(int, input().split()))
  square[x][y] = -1

# 움직임 deque에 넣기
move_n = int(input())
move_dq = deque([])
for i in range(move_n):
  after_sec, dir_change = input().split()
  move_dq.append([int(after_sec), dir_change])
  

dirIdx = 0
dirDic = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# R D L U
def rotate_dir(dirIdx, rotate):
  if rotate == "L":
    if dirIdx == 0:
      dirIdx = 3
    else:
      dirIdx -= 1
  if rotate == "D":
    if dirIdx == 3:
      dirIdx = 0
    else:
      dirIdx += 1
  return dirIdx

body_dq = deque([[1, 1]])
now = [1, 1]
sec = 0

next_move = None
if move_dq:
  next_move = move_dq.popleft()
  
while True:
  sec += 1
  print(sec)
    
  # 다음 갈 곳 확인
  x, y = dirDic[dirIdx]
  now_X, now_Y = now
  new_X, new_Y = now_X + x, now_Y + y
  # 이미 1인 곳이면 겜 끝
  if new_X > n or new_X < 1 or new_Y > n or new_Y < 1:
    print(sec)
    break
  elif square[new_Y][new_X] == 1:
    print(sec)
    break
  # 괜찮으면 body에 하나 추가, square 리스트 해당 좌표 0 -> 1 변환
  else:
    # 사과 아니라면 전체 길이 스택에서 하나 빼주기
    if square[new_Y][new_X] != -1:
      remove_X, remove_Y = body_dq.popleft()
      square[remove_Y][remove_X] = 0
      # 길이 스택에 하나 넣어주기
    body_dq.append([new_X, new_Y])
    square[new_Y][new_X] = 1
    now = [new_X, new_Y]

  # next_move 없고 move_dq 하나 이상 있다면 popLeft
  if not next_move and len(move_dq) > 0 :
    next_move = move_dq.popleft()
  # 마지막 : 스택에서 0번째 원소랑 sec이랑 같으면 방향 전환
  if next_move and next_move[0] == sec:
    dirIdx = rotate_dir(dirIdx, next_move[1])
    next_move = None
    # x, y = dirDic[0]
  # rotate_dir(dirIdx, )
  # for i in square:
  #   print(i)