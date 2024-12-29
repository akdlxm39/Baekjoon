import sys
from collections import deque
input = sys.stdin.readline

def main():
    N = int(input())
    stones = list(map(int, input().split()))
    a, b = map(lambda x: int(x)-1, input().split())
    q = deque()
    visited = [False]*N
    q.append((a, 0))
    while q:
        now, cnt = q.popleft()
        if now == b:
            print(cnt)
            break
        visited[now] = True
        left = now - stones[now]
        while 0 <= left:
            if visited[left] == False:
                q.append((left, cnt+1))
            left -= stones[now]
        right = now + stones[now]
        while right < N:
            if visited[right] == False:
                q.append((right, cnt+1))
            right += stones[now]
    else:
        print(-1)

if __name__ == "__main__":
    main()