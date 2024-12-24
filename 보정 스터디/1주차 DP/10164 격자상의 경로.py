import sys
input = sys.stdin.readline

def solve(x, y):
    dp = [1]*y
    for _ in range(x-1):
        for i in range(1, y):
            dp[i] = dp[i] + dp[i-1]
    return dp[-1]

def main():
    N, M, K = map(int, input().split())
    if K != 0:
        x, y = (K-1)//M, (K-1)%M
        print(solve(x+1, y+1) * solve(N-x, M-y))
    else:
        print(solve(N, M))


if __name__ == "__main__":
    main()