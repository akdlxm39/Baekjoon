import sys
input = sys.stdin.readline
N = int(input())
atWork = set()
for _ in range(N):
    name, check = input().split()
    if check == 'enter':
        atWork.add(name)
    else:
        atWork.discard(name)
for name in sorted(atWork, reverse=True):
    print(name)