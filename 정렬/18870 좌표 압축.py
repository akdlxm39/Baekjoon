import sys
input = sys.stdin.readline
N = int(input())
l = list(map(int, input().split()))
d = dict(zip(sorted(set(l)), range(len(set(l)))))
print(*[d[x] for x in l])