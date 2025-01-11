import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    gap = sorted([h[i] - h[i-1] for i in range(1, len(h))])
    print(sum(gap[:n-k]))

if __name__ == "__main__":
    main()