import sys
input = sys.stdin.readline
N = int(input())
words = sorted(set(input().rstrip() for _ in range(N)), key=lambda w:(len(w),w))
for word in words:
    print(word)