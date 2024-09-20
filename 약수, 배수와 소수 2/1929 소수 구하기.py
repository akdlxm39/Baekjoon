import sys
input = sys.stdin.readline

size = 1000000
primes = [False] * 2 + [True] * (size-1)
for i in range(2, int(size**0.5)+1):
    if primes[i] == False:
        continue
    primes[2*i:size+1:i] = [False] * (size//i-1)

M, N = map(int, input().split())
for i in range(M, N+1):
    if primes[i]:
        print(i)