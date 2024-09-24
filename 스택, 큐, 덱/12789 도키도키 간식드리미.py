import sys
input = sys.stdin.readline

N = int(input())
line = map(int, input().split())
idx = 1
stack = []
for s in line:
    stack.append(s)
    while stack and idx == stack[-1]:
        stack.pop()
        idx += 1
if stack:
    print("Sad")
else:
    print("Nice")