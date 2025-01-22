import sys
input = sys.stdin.readline

def solve(n, size, k):
    if k == 0:
        return "o" if n else "m"
    m1 = size[k-1]
    m2 = m1 + k + 3
    if m2 <= n:
        return solve(n - m2, size, k - 1)
    elif n < m1:
        return solve(n, size, k - 1)
    else:
        return solve(n - m1, size, 0)

# L(k) = 2 * L(K-1) + k + 3
# L(k) = 2^k * L(0) + sum(1~k) + 3*k

def main():
    n = int(input()) - 1
    k = 0
    size = [3]
    while size[-1] <= n:
        size.append(2 * size[-1] + k + 4)
        k += 1
    print(solve(n, size, k))

if __name__ == "__main__":
    main()