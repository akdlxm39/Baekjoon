import sys
input = sys.stdin.readline
# from bisect import bisect_left, bisect_right

def main():
    N = int(input())
    cards = sorted(map(int, input().split()))
    M = int(input())
    nums = list(map(int, input().split()))
    answer = []
    for num in nums:
        l = binary_search(N, cards, num)
        r = binary_search(N, cards, num+1)
        # l = bisect_left(cards, num)
        # r = bisect_right(cards, num)
        answer.append(r-l)
    print(' '.join(map(str, answer)))

def binary_search(N, cards, x):
    l, r = 0, N
    while l<r:
        m = (l+r)//2
        if cards[m] < x:
            l = m+1
        else:
            r = m
    return r

main()