import sys
input = sys.stdin.readline
N, M = map(int, input().split())
unheard = set(input().rstrip() for _ in range(N))
unknown = []
for _ in range(M):
    unseen = input().rstrip()
    if unseen in unheard:
        unknown.append(unseen)
print(len(unknown))
for name in sorted(unknown):
    print(name)