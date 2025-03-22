import sys
input = sys.stdin.readline

def main():
    n, m = int(input()), int(input())
    lines = dict()
    pre = 0
    for i in range(1, m+1):
        a, b = map(int, input().split())
        if a > b:
            pre = max(pre, b)
            b += n
        if a not in lines or lines[a][0] < b:
            lines[a] = (b, i)
    ans = []
    for _, (cur, i) in sorted(lines.items()):
        if pre < cur:
            ans.append(i)
            pre = cur
    print(*sorted(ans))

if __name__ == "__main__":
    main()