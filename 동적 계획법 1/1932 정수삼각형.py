import sys
input = sys.stdin.readline

def main():
    N = int(input())
    cur = list(map(int, input().split()))
    for _ in range(N-1):
        now = list(map(int, input().split()))
        cur = [max(cur[i-1]+x if i-1>=0 else 0, cur[i]+x if i<len(now)-1 else 0) for i, x in enumerate(now)]
    print(max(cur))

main()