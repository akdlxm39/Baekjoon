import sys
input = sys.stdin.readline
l = [True] * 30
for _ in range(28):
    i = int(input())
    l[i-1] = False
print('\n'.join(str(i) for i, b in enumerate(l, 1) if b))