import sys
input = sys.stdin.readline

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    dp1 = [1] * N
    dp2 = [1] * N
    for i in range(1, N):
        dp1[i] = 1 + max([0] + [dp1[j] for j in range(i) if nums[j]<nums[i]])
    for i in range(N-1, -1,-1):
        dp2[i] = 1 + max([0] + [dp2[j] for j in range(N-1, i-1, -1) if nums[j]<nums[i]])
    print(max(map(sum, zip(dp1, dp2)))-1)
    
main()