import sys
input = sys.stdin.readline
from math import factorial
T = int(input())
for _ in range(T):
    K, N = map(int, input().split())
    print(factorial(N)//factorial(K)//factorial(N-K))