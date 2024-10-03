import sys
input = sys.stdin.readline

# def main():
#     N = int(input())
#     paints = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(1, N):
#         paints[i][0] += min(paints[i-1][1], paints[i-1][2])
#         paints[i][1] += min(paints[i-1][0], paints[i-1][2])
#         paints[i][2] += min(paints[i-1][0], paints[i-1][1])
#     print(min(paints[N-1]))

def main():
    N = int(input())
    R, G, B = list(map(int, input().split()))
    for _ in range(N-1):
        r, g, b = list(map(int, input().split()))
        R, G, B = r + min(G, B), g + min(R, B), b + min(R, G)
    print(min(R, G, B))

main()