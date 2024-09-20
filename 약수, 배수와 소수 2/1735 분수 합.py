import sys
input = sys.stdin.readline
gcd = lambda a, b: a if b == 0 else gcd(b, a%b)
a, b = map(int, input().split())
c, d = map(int, input().split())
e = a*d + c*b
f = b*d
x = gcd(e, f)
print(e//x, f//x)