import sys
input = sys.stdin.readline
from collections import deque
R, C = map(int, input().split())
lake = [[] for _ in range(R)]
L = []
for i in range(R):
    line = input().rstrip()
    j = line.find('L')
    if j != -1:
        L.append((i, j))
    lake[i] = list(line)
print(L)
for l in lake:
    print(l)

q = deque()
q.append((L[0], 0))
while q:
    now = q.popleft()
    nr, nc = now[0]
    d = now[1]
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        r, c = nr+dr, nc+dc
        if 0<=r<R and 0<=c<C:
            if lake[r][c] == '.':
                q.append(((r,c), d))
            elif lake[r][c] == 'X':
                q.append(((r,c), d+1))
                




    













# class MiniLake:
#     def __init__(self, index = 0, lake = [], L = None) -> None:
#         self.index = index
#         self.lake = lake
#         self.L = L


# visited = [[False]*C for _ in range(R)]
# index = 0
# for r in range(R):
#     for c in range(C):
#         if lake[r][c] != '.':
#             continue
#         q = [(r,c)]
#         lake[r][c] = index
#         i = 0
#         while i < len(q):
#             ir, ic = q[i]
#             for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
#                 cr, cc = ir+dr, ic+dc
#                 if 0<=cr<R and 0<=cc<C and lake[cr][cc] == '.':
#                     q.append((cr,cc))
#                     lake[cr][cc] = index
#                 i += 1
                    




