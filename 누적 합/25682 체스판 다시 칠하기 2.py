import sys
input = sys.stdin.readline

def main():
    N, M, K = map(int, input().split())
    prefixsum = [[0]*(M+1) for _ in range(N+1)]
    check = 'BW'
    for i in range(1, N+1):
        line = input().rstrip()
        for j, c in enumerate(line, 1):
            prefixsum[i][j] = int(c != check[(i+j)%2]) + prefixsum[i-1][j] + prefixsum[i][j-1] - prefixsum[i-1][j-1]
    answer = K*K
    for i in range(K, N+1):
        for j in range(K, M+1):
            tmp = prefixsum[i][j] - prefixsum[i-K][j] - prefixsum[i][j-K] + prefixsum[i-K][j-K]
            answer = min(answer, tmp, K*K-tmp)
    print(answer)
    
main()