import sys
input = sys.stdin.readline

def n_queen(n, i, cant):
    if i == n:
        return 1
    res = 0
    for j in range(n):
        if cant[0][j] or cant[1][i+j] or cant[2][n-1+i-j]:
            continue
        cant[0][j] = cant[1][i+j] = cant[2][n-1+i-j] = True
        res += n_queen(n, i+1, cant)
        cant[0][j] = cant[1][i+j] = cant[2][n-1+i-j] = False
    return res

def main():
    n = int(input())
    ans = n_queen(n, 0, [[False]*n, [False]*(2*n-1), [False]*(2*n-1)])
    print(ans)

if __name__ == "__main__":
    main()