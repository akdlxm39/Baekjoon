import sys
input = sys.stdin.readline

def checkPrime(p):
    if p <= 1:
        return False
    for x in range(2, int(p**0.5)+1):
        if p % x == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    for p in range(N, 2*N+3):
        if checkPrime(p):
            print(p)
            break