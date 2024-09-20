import sys
input = sys.stdin.readline
gcd = lambda a, b: a if b == 0 else gcd(b, a%b)
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(a* b // gcd(a, b))