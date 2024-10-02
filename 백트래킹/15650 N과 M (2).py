import sys
input = sys.stdin.readline

def dfs(N, M, list, used):
    if M == 0:
        print(' '.join(map(str, list)))
        return
    for i in range(list[-1] if list else 0, N):
        if used[i]:
            continue
        used[i] = True
        dfs(N, M-1, list + [i + 1], used)
        used[i] = False

def main():
    N, M = map(int, input().split())
    dfs(N, M, [], [False]*N)

main()