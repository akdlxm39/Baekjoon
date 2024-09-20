import sys
input = sys.stdin.readline
N, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
print(l[k-1])