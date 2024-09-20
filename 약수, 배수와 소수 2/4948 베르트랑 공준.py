import sys
input = sys.stdin.readline

size = 123456*2
primes = [False] * 2 + [True] * (size-1)
for i in range(2, int(size**0.5)+1):
    if primes[i] == False:
        continue
    primes[2*i:size+1:i] = [False] * (size//i-1)

while True:
    N = int(input())
    if N == 0:
        break
    print(primes[N+1:2*N+1].count(True))