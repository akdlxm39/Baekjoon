import sys
input = sys.stdin.readline
S = input().rstrip()
l = [-1] * 26
for i in range(26):
    l[i] = S.find(chr(97 + i))
print(*l)