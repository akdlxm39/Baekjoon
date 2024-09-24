import sys
input = sys.stdin.readline

stack = []
K = int(input())
for _ in range(K):
    X = int(input())
    if X:
        stack.append(X)
    else:
        stack.pop()
print(sum(stack))
