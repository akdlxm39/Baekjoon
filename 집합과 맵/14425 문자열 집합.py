import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = set(input().rstrip() for _ in range(N))
answer = 0
for _ in range(M):
    if input().rstrip() in S:
        answer += 1
print(answer)