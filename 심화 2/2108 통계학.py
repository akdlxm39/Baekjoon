import sys
input = sys.stdin.readline
from collections import Counter
N = int(input())
nums = sorted(int(input()) for _ in range(N))
print(round(sum(nums)/len(nums)))
print(nums[len(nums)//2])
x = Counter(nums).most_common(2)
print(x[0][0] if len(x) == 1 or x[0][1] != x[1][1] else x[1][0])
print(max(nums)-min(nums))