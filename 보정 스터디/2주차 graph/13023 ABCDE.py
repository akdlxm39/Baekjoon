import sys
input = sys.stdin.readline

def solve(friends, visited, x, cnt):
    if cnt == 5:
        return True
    visited[x] = True
    for f in friends[x]:
        if visited[f]:
            continue
        if solve(friends, visited, f, cnt + 1):
            return True
    visited[x] = False
    return False

def main():
    N, M = map(int, input().split())
    friends = [[] for _ in range(N)]
    visited = [False] * N
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
    for i in range(N):
        if solve(friends, visited, i, 1):
            print(1)
            break
    else:
        print(0)

if __name__ == "__main__":
    main()