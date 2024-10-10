import sys
input = sys.stdin.readline

def main():
    N = int(input())
    k = int(input())
    answer = binary_search(N, k)
    print(answer)

def binary_search(N, k):
    l, r = 1, N*N
    while l<=r:
        m = (l+r)//2
        if check(N, m) < k:
            l = m+1
        else:
            r = m-1
    return l

def check(N, m):
    result = 0
    for i in range(1, min(m+1, N+1)):
        result += min(m//i, N)
    return result

main()