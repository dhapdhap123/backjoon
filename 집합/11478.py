import sys
input = sys.stdin.readline
from collections import deque

string = input().rstrip()
# i는 시작 인덱스
asw = set({})
for i in range(len(string)):
    # j는 길이
    for j in range(1, len(string) + 1):
        part = string[i:i+j]
        if part not in asw:
            asw.add(string[i:i+j])
print(len(asw))