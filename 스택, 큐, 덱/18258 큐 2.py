import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N):
    L = input().rstrip()
    if L[:4] == "push":
        queue.append(int(L[5:]))
    elif L == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif L == "size":
        print(len(queue))
    elif L == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif L == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif L == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        print("Error")