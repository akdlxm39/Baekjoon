import sys
input = sys.stdin.readline

size = 10000
primes = [False] * 2 + [True] * (size-1)
for i in range(2, int(size**0.5)+1):
    if primes[i] == False:
        continue
    primes[2*i:size+1:i] = [False] * (size//i-1)

M = int(input())
N = int(input())
mnPrimes = [i for i, b in enumerate(primes[M:N+1], M) if b]
if mnPrimes:
    print(sum(mnPrimes))
    print(min(mnPrimes))
else:
    print(-1)