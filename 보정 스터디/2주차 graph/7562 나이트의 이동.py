import sys
from collections import deque
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        l = int(input())
        s = tuple(map(int, input().split()))
        e = tuple(map(int, input().split()))
        q = deque()
        visited = [[False]*l for _ in range(l)]
        q.append((s[0], s[1], 0))
        visited[s[0]][s[1]] = True
        while q:
            x, y, cnt = q.popleft()
            if e == (x, y):
                print(cnt)
                break
            for dx, dy in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < l and 0 <= ny < l and visited[nx][ny]==False:
                    q.append((nx, ny, cnt+1))
                    visited[nx][ny] = True

if __name__ == "__main__":
    main()