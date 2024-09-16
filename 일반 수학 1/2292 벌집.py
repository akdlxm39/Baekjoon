import sys
input = sys.stdin.readline
N = int(input())
N -= 1
i = 0
while N > 6*i:
    N -= 6*i
    i += 1
print(i+1)