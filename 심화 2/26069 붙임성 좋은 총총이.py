import sys
input = sys.stdin.readline

N = int(input())
s = {"ChongChong"}
for _ in range(N):
    A, B = input().split()
    if A in s:
        s.add(B)
    elif B in s:
        s.add(A)
print(len(s))