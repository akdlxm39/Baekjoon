import sys
input = sys.stdin.readline
N = int(input())
members = []
for _ in range(N):
    age, name = input().split()
    age = int(age)
    members.append((age, name))
members.sort(key=lambda m:m[0])
for m in members:
    print(*m)