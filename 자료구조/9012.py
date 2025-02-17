import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
  stack = []
  flag = "YES"
  str = input()
  for j in str:
    # print(stack)
    if j == "(":
      stack.append("(")
    elif j == ")":
      if len(stack) == 0:
        flag = "NO"
        break
      else:
        last = stack.pop()
  if len(stack) != 0:
    flag = "NO"
  print(flag)