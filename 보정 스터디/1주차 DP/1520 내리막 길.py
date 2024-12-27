import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(Map, dp, M, N, x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    s = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and Map[nx][ny] > Map[x][y]:
            s += solve(Map, dp, M, N, nx, ny)
    dp[x][y] = s
    return s

def main():
    M, N = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(M)]
    dp = [[-1]*N for _ in range(M)]
    dp[0][0] = 1
    print(solve(Map, dp, M, N, M-1, N-1))

if __name__ == "__main__":
    main()