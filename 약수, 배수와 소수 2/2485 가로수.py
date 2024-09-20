import sys
input = sys.stdin.readline
gcd = lambda a, b: a if b == 0 else gcd(b, a%b)
N = int(input())
l = [int(input()) for _ in range(N)]
gap = l[1] - l[0]
for t1, t2 in zip(l[1:], l[2:]):
    gap = gcd(gap, t2-t1)
print((l[-1]-l[0])//gap - len(l) + 1)