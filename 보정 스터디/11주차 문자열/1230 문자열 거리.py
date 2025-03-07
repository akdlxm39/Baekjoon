import sys
input = sys.stdin.readline

def main():
    o = input().rstrip()
    n = input().rstrip()
    dp = [(0, True)] + [(0, False) for _ in range(len(n))]
    for x in o:
        tmp = [(0, False)]
        mindp = 1000
        for i, y in enumerate(n, 1):
            if dp[i-1][1]:
                mindp = min(mindp, dp[i-1][0])
            if x == y:
                if dp[i-1][1]:
                    tmp.append((dp[i-1][0], True))
                elif mindp != 1000:
                    tmp.append((mindp+1, True))
                else:
                    tmp.append((0, False))
            else:
                tmp.append((0, False))
        dp = tmp
    ans = [x + 1 for x, b in dp[:-1] if b]
    if dp[-1][1]:
        ans.append(dp[-1][0])
    print(min(ans) if ans else -1)

if __name__ == "__main__":
    main()