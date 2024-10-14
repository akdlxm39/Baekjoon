import sys
input = sys.stdin.readline
import heapq

def main():
    T = int(input())
    for _ in range(T):
        K = int(input())
        arr = [0] + list(map(int, input().split()))
        for i in range(2, K+1):
            arr[i] += arr[i-1]
        dp = [[0]*K for _ in range(K)]
        opt = [[0]*K for _ in range(K)]
        for i in range(K):
            opt[i][i] = i
            for j in range(i-1, -1, -1):
                dp[j][i] = 100000000
                for k in range(opt[j][i-1], opt[j+1][i]+1):
                    if k+1 < K and dp[j][i] > dp[j][k] + dp[k+1][i]:
                        dp[j][i] = dp[j][k] + dp[k+1][i]
                        opt[j][i] = k
                dp[j][i] += arr[i+1] - arr[j]
                # dp[j][i] = min(dp[j][k] + dp[k+1][i] for k in range(j, i)) + arr[i+1] - arr[j]
        print(dp[0][K-1])

main()