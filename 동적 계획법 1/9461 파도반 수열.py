import sys
input = sys.stdin.readline

def main():
    T = int(input())
    dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90
    for i in range(11, 101):
        dp[i] = dp[i-5] + dp[i-1]
    for _ in range(T):
        N = int(input())
        print(dp[N])

main()