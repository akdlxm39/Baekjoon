import sys
input = sys.stdin.readline

def main():
    n = int(input())
    wines = [int(input()) for _ in range(n)]
    dp = [[0, 0] for _ in range(n+3)]
    for i, w in enumerate(wines, 3):
        dp[i][0] = max(dp[i-3][0], dp[i-3][1], dp[i-2][0], dp[i-2][1]) + w
        dp[i][1] = dp[i-1][0] + w
    print(max(dp[-1] + dp[-2]))

if __name__ == "__main__":
    main()