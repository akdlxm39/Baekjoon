import sys
input = sys.stdin.readline
# from bisect import bisect_left

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [nums[0]]
    for num in nums[1:]:
        if dp[-1] < num:
            dp.append(num)
        else:
            # dp[bisect_left(dp, num)] = num
            dp[binary_search(dp, num)] = num
    print(len(dp))

def binary_search(dp, num):
    l, r = 0, len(dp)-1
    while l<=r:
        m = (l+r)//2
        if dp[m] < num:
            l = m+1
        elif dp[m] > num:
            r = m-1
        else:
            return m
    return l

main()