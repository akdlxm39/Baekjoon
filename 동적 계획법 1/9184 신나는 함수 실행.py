import sys
input = sys.stdin.readline

def w(a, b, c, dp):
    if a<=0 or b<=0 or c<=0:
        dp[0][0][0] = 1
        return dp[0][0][0]
    if a>20 or b>20 or c>20:
        return w(20, 20, 20, dp)
    if dp[a][b][c] != -1:
        return dp[a][b][c]
    if a<b and b<c:
        dp[a][b][c] = w(a, b, c-1, dp) + w(a, b-1, c-1, dp) - w(a, b-1, c, dp)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c, dp) + w(a-1, b-1, c, dp) + w(a-1, b, c-1, dp) - w(a-1, b-1, c-1, dp)
        return dp[a][b][c]

def main():
    dp = [[[-1]*21 for _ in range(21)] for _ in range(21)]
    while True:
        a, b, c = map(int, input().split())
        if a==-1 and b==-1 and c==-1:
            break
        print(f"w({a}, {b}, {c}) = {w(a, b, c, dp)}")

main()