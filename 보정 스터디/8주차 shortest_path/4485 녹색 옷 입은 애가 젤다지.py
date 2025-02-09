import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline
INF = 1e9
delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def main():
    idx = 0
    while n := int(input()):
        idx += 1
        maps = [list(map(int, input().split())) for _ in range(n)]
        dp = [[INF] * n for _ in range(n)]
        dp[0][0] = maps[0][0]
        heap = [(dp[0][0], 0, 0)]
        while heap:
            cost, cx, cy = heappop(heap)
            if cx == 1-n and cy == 1-n:
                print(f"Problem {idx}: {cost}")
                break
            for dx, dy in delta:
                nx, ny = -cx + dx, -cy + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                next_cost = cost + maps[nx][ny]
                if next_cost < dp[nx][ny]:
                    dp[nx][ny] = next_cost
                    heappush(heap, (next_cost, -nx, -ny))


if __name__ == "__main__":
    main()