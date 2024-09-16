import sys
input = sys.stdin.readline
paper = [[False]*100 for _ in range(100)]
for _ in range(int(input())):
    X, Y = map(int, input().split())
    for i in range(X, X + 10):
        paper[i][Y:Y+10] = [True]*10
answer = 0
for p in paper:
    for b in p:
        answer += int(b)
print(answer)