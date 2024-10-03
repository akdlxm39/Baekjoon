import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [0] * (K+1)
    for w, v in items:
        # dp = dp[:w] + [max(dp[i], dp[i-w] + v) for i in range(w, K+1)]
        for i in range(K, w-1, -1):
            dp[i] = max(dp[i], dp[i-w] + v)
    print(max(dp))

main()