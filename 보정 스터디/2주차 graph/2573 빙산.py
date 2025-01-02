import sys
from collections import deque
input = sys.stdin.readline

def check(ice):
    n, m = len(ice), len(ice[0])
    visited = [[False]*m for _ in range(n)]
    q = deque()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] or ice[i][j] == 0:
                continue
            q.append((i, j))
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if visited[nx][ny] or ice[nx][ny] == 0:
                        continue
                    q.append((nx, ny))
                    visited[nx][ny] = True
            cnt += 1
    return cnt

def solve(ice, adj_sea):
    n, m = len(ice), len(ice[0])
    new_ice = [[0]*m for _ in range(n)]
    new_adj_sea = [[x for x in l] for l in adj_sea]
    for i in range(n):
        for j in range(m):
            if ice[i][j] == 0:
                continue
            new_ice[i][j] = max(0, ice[i][j] - adj_sea[i][j])
            if new_ice[i][j] == 0:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0<=ni<n and 0<=nj<m:
                        new_adj_sea[ni][nj] += 1
    return new_ice, new_adj_sea

def main():
    N, M = map(int, input().split())
    ice = [list(map(int, input().split())) for _ in range(N)]

    adj_sea = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            cnt = 0
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0<=ni<N and 0<=nj<M and ice[ni][nj] == 0:
                    cnt += 1
            adj_sea[i][j] = cnt

    answer = 0
    while True:
        ice, adj_sea = solve(ice, adj_sea)
        cnt = check(ice)
        answer += 1
        if cnt > 1:
            print(answer)
            break
        elif cnt == 0:
            print(0)
            break

if __name__ == "__main__":
    main()