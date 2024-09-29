import sys
input = sys.stdin.readline

def fibonacci(N):
    if N <= 1:
        return N
    return fibonacci(N-1) + fibonacci(N-2)

def main():
    N = int(input())
    print(fibonacci(N))

main()