import sys
input = sys.stdin.readline

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [1] * N
    for i in range(1, N):
        dp[i] = 1 + max([0] + [dp[j] for j in range(i) if nums[j]<nums[i]])
    print(max(dp))
    
main()