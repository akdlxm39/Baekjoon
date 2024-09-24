import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
check = list(map(int, input().split()))
qlist = [x for i, x in enumerate(map(int, input().split())) if check[i] == 0]
qlist.reverse()
M = int(input())
X = list(map(int, input().split()))
print(*(qlist+X)[:M])