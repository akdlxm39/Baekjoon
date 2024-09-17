import sys
input = sys.stdin.readline
N, K = map(int, input().split())
factors = []
for x in range(1, N+1):
    if N % x == 0:
        factors.append(x)
print(factors[K-1] if len(factors) >= K else 0)