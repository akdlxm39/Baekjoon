import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    prefixsum = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        nums = map(int, input().split())
        for j, n in enumerate(nums, 1):
            prefixsum[i][j] = n + prefixsum[i-1][j] + prefixsum[i][j-1] - prefixsum[i-1][j-1]
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        print(prefixsum[x2][y2] - prefixsum[x1-1][y2] - prefixsum[x2][y1-1] + prefixsum[x1-1][y1-1])

main()