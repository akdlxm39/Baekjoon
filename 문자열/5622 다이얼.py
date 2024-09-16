import sys
input = sys.stdin.readline
S = input().rstrip()
dial = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
T = sum(dial[ord(x)-65]+1 for x in S)
print(T)