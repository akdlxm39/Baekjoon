import sys
input = sys.stdin.readline
N, X = map(int, input().split())
l = [i for i in map(int, input().split()) if i < X]
print(*l)