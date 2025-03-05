import sys
input = sys.stdin.readline

def main():
    o = input().rstrip()
    n = input().rstrip()
    dp = [[[0, False] for _ in range(len(n)+1)] for _ in range(len(o)+1)]
    dp[0][0][1] = True
    for i, x in enumerate(o, 1):
        for j, y in enumerate(n, 1):
            if x == y:
                if dp[i-1][j-1][1]:
                    dp[i][j][0] = dp[i-1][j-1][0]
                    dp[i][j][1] = True
                else:
                    tmp = [x[0] for x in dp[i-1][:j-1] if x[1]]
                    if tmp:
                        dp[i][j][0] = min(tmp)+1
                        dp[i][j][1] = True
    for i, l in enumerate(dp):
        for j, x in enumerate(l):
            if i == 0 and j > 0:
                print(n[j-1], end=' ')
            elif j == 0 and i > 0:
                print(o[i-1], end=' ')
            else:
                print(('\033[90m' if x[1]==False else '') + str(x[0]) + '\033[0m', end=' ')
        print()
    ans = len(n)
    for i in range(1, len(n)+2):
        if i == len(n)+1:
            if dp[-1][-1][1]:
                ans = min(ans, dp[-1][-1][0])
            break
        if dp[-1][i][1]:
            ans = min(ans, dp[-1][i][0]+1)
    print(ans if ans!=len(n) else -1)

if __name__ == "__main__":
    main()