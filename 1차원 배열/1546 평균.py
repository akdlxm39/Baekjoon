import sys
input = sys.stdin.readline
N = int(input())
l = list(map(int, input().split()))
answer = sum(l) / len(l) / max(l) * 100
print(answer)