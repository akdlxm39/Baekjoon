import sys
input = sys.stdin.readline
X = [list(map(int, input().split())) for _ in range(9)]
M = -1
answer = (0, 0)
for i in range(9):
    for j in range(9):
        if X[i][j] > M:
            M = X[i][j]
            answer = (i+1, j+1)
print(M)
print(*answer)