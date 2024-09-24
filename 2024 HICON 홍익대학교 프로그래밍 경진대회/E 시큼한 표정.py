import sys
from math import factorial as fact
input = sys.stdin.readline


def coin(t, b):
    return (fact(t+b)//fact(t)//fact(b))%1000000007

N = int(input())
S = input().rstrip()
center = set()
for i in range(N-1):
    if S[i:i+2] == '><':
        center.add(i+1)


answer = 0
for x in range(1,N//2-len(center)+2):
    for c in center:
        if S[c-x:c+x] == ('>'*x + '<'*x):
            left = c-x
            right = N-c-x
            answer = (answer + coin(left, right)) % 1000000007
print(answer)
