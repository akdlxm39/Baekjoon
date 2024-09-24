import sys
input = sys.stdin.readline

stack = []
N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    if A[0] == 1:
        stack.append(A[1])
    elif A[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif A[0] == 3:
        print(len(stack))
    elif A[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif A[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        print("Error")
