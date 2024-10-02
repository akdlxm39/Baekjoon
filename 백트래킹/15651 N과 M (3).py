import sys
input = sys.stdin.readline

def dfs(N, M, list):
    if M == 0:
        print(' '.join(map(str, list)))
        return
    for i in range(N):
        dfs(N, M-1, list + [i + 1])

def main():
    N, M = map(int, input().split())
    dfs(N, M, [])

main()