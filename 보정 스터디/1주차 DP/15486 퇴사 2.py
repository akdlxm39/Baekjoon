import sys
input = sys.stdin.readline

def main():
    N = int(input())
    counsel = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [0]*(N+1)
    M = 0
    for i, (t, p) in enumerate(counsel, 1):
        if i+t-1 <= N:
            dp[i+t-1] = max(dp[i+t-1], M + p)
        M = max(M, dp[i])
    print(M)

if __name__ == "__main__":
    main()