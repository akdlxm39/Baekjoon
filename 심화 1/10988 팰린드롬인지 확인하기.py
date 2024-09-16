import sys
input = sys.stdin.readline
S = input().rstrip()
print(1 if S == S[::-1] else 0)