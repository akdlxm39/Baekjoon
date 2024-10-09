import sys
input = sys.stdin.readline

MOD = 1000000007

def main():
    N, K = map(int, input().split())
    numerator = 1
    denominator = 1
    for i in range(N-K+1, N+1):
        numerator = numerator * i % MOD
    for i in range(1, K+1):
        denominator = denominator * i % MOD
    answer = numerator * power(denominator, MOD-2) % MOD
    print(answer)

def power(X, e):
    if e == 1:
        return X % MOD
    return (power(X, e//2) ** 2) * X % MOD if e%2 else power(X, e//2) ** 2 % MOD

main()