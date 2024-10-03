import sys
input = sys.stdin.readline

# def main():
#     N = int(input())
#     dp = [1, 1] + [0] * (N-1)
#     for i in range(2, N+1):
#         dp[i] = (dp[i-1] + dp[i-2]) % 15746
#     print(dp[N])

def main():
    N = int(input())
    a, b = 0, 1
    for _ in range(N):
        a, b = b, (a + b) % 15746
    print(b)

main()