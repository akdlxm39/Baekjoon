import sys
from collections import deque
input = sys.stdin.readline

dq = deque()
N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    if A[0] == 1:
        dq.appendleft(A[1])
    elif A[0] == 2:
        dq.append(A[1])
    elif A[0] == 3:
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif A[0] == 4:
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif A[0] == 5:
        print(len(dq))
    elif A[0] == 6:
        if dq:
            print(0)
        else:
            print(1)
    elif A[0] == 7:
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif A[0] == 8:
        if dq:
            print(dq[-1])
        else:
            print(-1)
    else:
        print("Error")
