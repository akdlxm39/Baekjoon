import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]
good_board = ["BWBWBWBW", "WBWBWBWB"]
answer = 32
for i in range(N-7):
    for j in range(M-7):
        count = 0
        for di in range(8):
            for dj in range(8):
                if board[i+di][j+dj] != good_board[di%2][dj]:
                    count += 1
        answer = min(answer, count, 64-count)
print(answer)