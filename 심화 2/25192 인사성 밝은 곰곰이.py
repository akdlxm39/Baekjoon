import sys
input = sys.stdin.readline

N = int(input())
s = set()
answer = 0
for _ in range(N):
    S = input().rstrip()
    if S == "ENTER":
        answer += len(s)
        s.clear()
    else:
        s.add(S)
print(answer + len(s))