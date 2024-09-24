import sys
input = sys.stdin.readline

R, C = map(int, input().split())
N = int(input())

d = dict()
for _ in range(N):
    a, v, h = map(int, input().split())
    if a in d:
        d[a].append((v,h))
    else:
        d[a] = [(v,h)]
max_size = 0
max_num = N
for i, p in d.items():
    x1 = y1 = 100000
    x2 = y2 = 0
    for x, y in p:
        x1 = min(x1, x)
        x2 = max(x2, x)
        y1 = min(y1, y)
        y2 = max(y2, y)
    size = (x2-x1+1) * (y2-y1+1)
    if size > max_size:
        max_size = size
        max_num = i
    elif size == max_size:
        max_num = min(max_num, i)
print(max_num, max_size)