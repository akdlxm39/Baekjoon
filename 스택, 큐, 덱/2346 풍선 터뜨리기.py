import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dq = deque((i, x) for i, x in enumerate(map(int, input().split()), 1))
answer = []
while dq:
    now, move = dq.popleft()
    answer.append(now)
    if dq and move > 0:
        for _ in range(move-1):
            dq.append(dq.popleft())
    elif dq and move < 0:
        for _ in range(-move):
            dq.appendleft(dq.pop())
print(*answer)