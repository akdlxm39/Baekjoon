import sys
input = sys.stdin.readline

def main():
    N, B = map(int, input().split())
    A = [[x % 1000 for x in map(int, input().split())] for _ in range(N)]
    answer = devide(A, B)
    print('\n'.join(' '.join(map(str, line)) for line in answer))

def devide(A, N):
    if N == 1:
        return A
    tmp1 = devide(A, N//2)
    tmp2 = matmul(tmp1, tmp1)
    return matmul(tmp2, A) if N % 2 else tmp2

def matmul(A, B):
    B1 = list(zip(*B))
    return [[sum((a * b)%1000 for a, b in zip(lineA, lineB))%1000 for lineB in B1] for lineA in A]

main()