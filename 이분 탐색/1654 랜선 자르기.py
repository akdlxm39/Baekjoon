import sys
input = sys.stdin.readline

def main():
    K, N = map(int, input().split())
    cables = [int(input()) for _ in range(K)]
    answer = binary_search(cables, N)
    print(answer)

def binary_search(cables, N):
    l, r = 0, 2**31-1
    while l<=r:
        m = (l+r)//2
        if check(cables, m) >= N:
            l = m+1
        else:
            r = m-1
    return r

def check(cables, m):
    result = 0
    for cable in cables:
        result += cable//m
    return result

main()