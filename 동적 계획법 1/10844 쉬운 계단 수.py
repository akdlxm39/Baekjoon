import sys
input = sys.stdin.readline

def main():
    N = int(input())
    dp = [0] + [1]*9
    for _ in range(N-1):
        dp = [((dp[j-1] if j>0 else 0) + (dp[j+1] if j<9 else 0)) % 1000000000 for j in range(10)]
    print(sum(dp) % 1000000000)

main()