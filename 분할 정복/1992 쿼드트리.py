import sys
input = sys.stdin.readline

def main():
    N = int(input())
    bitmap = [input().rstrip() for _ in range(N)]
    answer = quadtree(bitmap, 0, 0, N)
    print(answer)

def quadtree(bitmap, x, y, size):
    if size == 1:
        return bitmap[x][y]
    half = size // 2
    bits = ""
    for dx, dy in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        bits += quadtree(bitmap, x+dx*half, y+dy*half, half)
    if bits == "0000" or bits == "1111":
        return bits[0]
    else:
        return "(" + bits + ")"

main()