import sys
input = sys.stdin.readline
A, B, C = sorted(map(int, input().split()))
print(A + B + min(A + B - 1, C))