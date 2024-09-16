import sys
from math import ceil
input = sys.stdin.readline
A, B, V = map(int, input().split())
answer = 1 + ceil((V-A)/(A-B))
print(answer)