import sys
input = sys.stdin.readline

def main():
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    count = [0, 0]
    cut(paper, 0, 0, N, count)
    print(f"{count[0]}\n{count[1]}")

def cut(paper, x, y, size, count):
    if size == 1:
        count[paper[x][y]] += 1
        return paper[x][y]
    half = size // 2
    colors = []
    for dx, dy in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        tmp = cut(paper, x+dx*half, y+dy*half, half, count)
        if tmp == 0 or tmp == 1:
            colors.append(tmp)
    if len(colors) == 4 and sum(colors)%4 == 0:
        count[colors[0]] -= 3
        return colors[0]

main()
