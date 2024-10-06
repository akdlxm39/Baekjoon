import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    prefixsum = sum(nums[:K])
    answer = prefixsum
    for i, j in zip(nums, nums[K:]):
        prefixsum += j - i
        answer = max(answer, prefixsum)
    print(answer)

main()