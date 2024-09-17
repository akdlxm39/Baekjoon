import sys
input = sys.stdin.readline

size = 1000
primes = [False] * 2 + [True] * (size-1)
for i in range(2, int(size**0.5)+1):
    if primes[i] == False:
        continue
    primes[2*i:size+1:i] = [False] * (size//i-1)

N = int(input())
nums = list(map(int, input().split()))
count = 0
for n in nums:
    if primes[n]:
        count += 1
print(count)