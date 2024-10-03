import sys
input = sys.stdin.readline

def main():
    N = int(input())
    dp = [0, 1, 1] + [0] * N
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N], N-2)

main()