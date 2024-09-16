import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    print(''.join([c * R for c in S]))