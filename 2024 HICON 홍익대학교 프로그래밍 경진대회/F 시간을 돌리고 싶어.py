import sys
from math import ceil
input = sys.stdin.readline

N, K = map(int, input().split())
on = list(map(int, input().split()))
s = 1

def bin_search(l, r):
    if l == r:
        return l
    m = (l+r)//2
    x = 0
    for o in on[1:]:
        if o == 1:
            pass
