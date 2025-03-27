import sys
input = sys.stdin.readline

def main():
    n = int(input())
    lines = [x for _,x in sorted(tuple(map(int, input().split())) for _ in range(n))]
    dp = []
    for i in range(n):
        dp.append(max([dp[j]+1 for j in range(i) if lines[j] < lines[i]] + [1]))
    print(n-max(dp))

if __name__ == "__main__":
    main()