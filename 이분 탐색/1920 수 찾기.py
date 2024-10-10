import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = sorted(map(int, input().split()))
    M = int(input())
    for x in map(int, input().split()):
        print(int(binary_search(N, A, x)))

def binary_search(N, A, x):
    l, r = 0, N-1
    while l<=r:
        m = (l+r)//2
        if A[m] == x:
            return True
        elif A[m] < x:
            l = m+1
        else:
            r = m-1
    return False

main()