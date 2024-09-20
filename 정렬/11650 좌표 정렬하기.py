import sys
input = sys.stdin.readline
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
points.sort()
for point in points:
    print(*point)