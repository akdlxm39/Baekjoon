import sys
input = sys.stdin.readline
from collections import deque

# def main():
#     N = int(input())
#     dp = [0] * (N+1)
#     for i in range(2, N+1):
#         dp[i] = 1 + min(dp[i-1], dp[i//2] if i%2==0 else dp[i-1], dp[i//3] if i%3==0 else dp[i-1])
#     print(dp[N])

def func(N, dp):
    if N in dp:
        return dp[N]
    dp[N] = 1 + min(func(N-1, dp) if N%6 else N, func(N//2, dp) if N%2==0 else N, func(N//3, dp) if N%3==0 else N)
    return dp[N]

def main():
    N = int(input())
    dp = {1:0}
    print(func(N, dp))


main()