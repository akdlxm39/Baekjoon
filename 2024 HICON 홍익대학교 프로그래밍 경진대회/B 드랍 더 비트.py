import sys
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
M = abs(a+b-N)
X = int('1' * (N-M) + '0' * M, 2)
print(X)