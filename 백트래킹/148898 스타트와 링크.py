import sys
input = sys.stdin.readline

def func2(stats, A, B):
    result = 0
    for i in A:
        for j in A:
            result += stats[i][j]
    for i in B:
        for j in B:
            result -= stats[i][j]
    return abs(result)

def func(N, stats, idx, A, B, M):
    if idx == N:
        M[0] = min(M[0], func2(stats, A, B))
        return
    if len(A) < N//2:
        func(N, stats, idx+1, A + [idx], B, M)
    if len(B) < N//2:
        func(N, stats, idx+1, A, B + [idx], M)

def main():
    N = int(input())
    stats = [list(map(int, input().split())) for _ in range(N)]
    M = [10000]
    func(N, stats, 0, [], [], M)
    print(M[0])

main()