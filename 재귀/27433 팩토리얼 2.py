import sys
input = sys.stdin.readline

def factorial(N):
    if N <= 1:
        return 1
    return N * factorial(N-1)

def main():
    N = int(input())
    print(factorial(N))

main()