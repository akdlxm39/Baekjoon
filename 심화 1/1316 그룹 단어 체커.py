import sys
input = sys.stdin.readline
N = int(input())
answer = 0
for _ in range(N):
    S = input().rstrip()
    tmp = [S[0]]
    for c in S:
        if c == tmp[-1]:
            continue
        elif c in tmp:
            break
        else:
            tmp.append(c)
    else:
        answer += 1
print(answer)