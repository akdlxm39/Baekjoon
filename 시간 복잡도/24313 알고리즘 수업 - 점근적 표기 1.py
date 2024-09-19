import sys
input = sys.stdin.readline
a, b = map(int, input().split())
c = int(input())
n0 = int(input())
print(int(a * n0 + b <= c * n0 and a <= c))