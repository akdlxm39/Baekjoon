import sys
input = sys.stdin.readline
N = int(input())
numCount = [0] * 10001
for _ in range(N):
    numCount[int(input())] += 1
for i, cnt in enumerate(numCount[1:], 1):
    for _ in range(cnt):
        print(i)