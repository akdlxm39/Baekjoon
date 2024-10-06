import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    prefixsum = [0] * (N+1)
    for i, num in enumerate(nums, 1):
        prefixsum[i] = prefixsum[i-1] + num
    for _ in range(M):
        l, r = map(int, input().split())
        print(prefixsum[r]-prefixsum[l-1])

main()