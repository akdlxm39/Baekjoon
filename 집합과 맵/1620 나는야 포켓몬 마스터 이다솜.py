import sys
input = sys.stdin.readline
N, M = map(int, input().split())
numToName = dict()
nameToNum = dict()
for num in range(1, N+1):
    name = input().rstrip()
    numToName[num] = name
    nameToNum[name] = num
for _ in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(numToName[int(q)])
    else:
        print(nameToNum[q])
