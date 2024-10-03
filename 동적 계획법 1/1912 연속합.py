import sys
input = sys.stdin.readline

# def main():
#     N = int(input())
#     nums = list(map(int, input().split()))
#     cur = 0
#     M = -1000
#     for num in nums:
#         cur = max(num, cur + num)
#         M = max(M, cur)
#     print(M)

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(1, N):
        nums[i] = max(nums[i], nums[i-1] + nums[i])
    print(max(nums))

main()