import sys
input = sys.stdin.readline
N = int(input())
for x in range(max(0, N-9*len(str(N))), N):
    tmp = x + sum(map(int, str(x)))
    if tmp == N:
        print(x)
        break
else:
    print(0)