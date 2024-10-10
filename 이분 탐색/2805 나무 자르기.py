import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    trees = sorted(map(int, input().split()))
    answer = binary_search(trees, M)
    print(answer)

def binary_search(trees, N):
    l, r = 0, trees[-1]
    while l<=r:
        m = (l+r)//2
        if check(trees, m) >= N:
            l = m+1
        else:
            r = m-1
    return r

def check(trees, m):
    result = sum(tree - m for tree in trees if tree > m)
    return result

main()