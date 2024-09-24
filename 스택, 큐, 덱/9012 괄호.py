import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = input().rstrip()
    stack = 0
    for c in S:
        if c == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            print("NO")
            break
    else:
        if stack:
            print("NO")
        else:
            print("YES")