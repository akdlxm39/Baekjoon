import sys
input = sys.stdin.readline
N = int(input())
l = list(map(int, input().split()))
print(min(l), max(l))