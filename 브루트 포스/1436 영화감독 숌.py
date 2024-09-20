import sys
input = sys.stdin.readline
N = int(input())
title = 0
for _ in range(N):
    while True:
        title += 1
        if '666' in str(title):
            break
print(title)