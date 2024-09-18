import sys
input = sys.stdin.readline
x1 = y1 = 10000
x2 = y2 = -10000
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    x1 = min(x1, x)
    x2 = max(x2, x)
    y1 = min(y1, y)
    y2 = max(y2, y)
print((x2-x1)*(y2-y1))