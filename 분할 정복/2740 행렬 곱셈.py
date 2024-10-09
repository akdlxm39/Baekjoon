import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    _, K = map(int, input().split())
    # B = [list(map(int, input().split())) for _ in range(M)]
    # answer = [[sum(A[n][m] * B[m][k] for m in range(M)) for k in range(K)] for n in range(N)]
    B = list(zip(*[list(map(int, input().split())) for _ in range(M)]))
    answer = [[sum(a * b for a, b in zip(lineA, lineB)) for lineB in B] for lineA in A]
    print('\n'.join(' '.join(map(str, line)) for line in answer))

main()