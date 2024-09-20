import sys
input = sys.stdin.readline
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
doHave = [int(x in cards) for x in map(int,input().split())]
print(*doHave)