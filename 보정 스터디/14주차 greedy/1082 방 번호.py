import sys
input = sys.stdin.readline

def main():
    n = int(input())
    pi = list(map(int, input().split()))
    m = int(input())
    cmp = lambda x: ((m - pi[x]) // pi[0], x)
    if n == 1:
        print(0)
        return
    ans = ''
    idx = max(range(1, n), key=cmp)
    while m>0:
        if pi[idx] > m:
            break
        ans += str(idx)
        m -= pi[idx]
        idx = max(range(n), key=cmp)
    if m>0:
        ans += '0'*(m//pi[0])
    print(int(ans))

if __name__ == "__main__":
    main()