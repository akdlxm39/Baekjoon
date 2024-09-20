import sys
input = sys.stdin.readline
N = int(input())
l = [int(input()) for _ in range(N)]
l.sort()
for x in l:
    print(x)