import sys
input = sys.stdin.readline

def main():
    N = int(input())
    rgb1 = list(map(int, input().split()))
    rgb2 = list(map(int, input().split()))
    rr, rg, rb, gr, gg, gb, br, bg, bb = [(rgb1[i]+rgb2[j]) if i!=j else 10000 for i in range(3) for j in range(3)]
    for i in range(2, N):
        r, g, b = map(int, input().split())
        rr, rg, rb = min(rg, rb) + r, min(rr, rb) + g, min(rr, rg) + b
        gr, gg, gb = min(gg, gb) + r, min(gr, gb) + g, min(gr, gg) + b
        br, bg, bb = min(bg, bb) + r, min(br, bb) + g, min(br, bg) + b
    print(min(rg, rb, gr, gb, br, bg))

if __name__ == "__main__":
    main()