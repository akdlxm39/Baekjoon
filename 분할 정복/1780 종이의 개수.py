import sys
input = sys.stdin.readline

def main():
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    count = [0, 0, 0]
    cut(paper, 0, 0, N, count)
    print(f"{count[0]}\n{count[1]}\n{count[2]}")

def cut(paper, x, y, size, count):
    if size == 1:
        count[paper[x][y]+1] += 1
        return paper[x][y]
    divide = size // 3
    nums = []
    for dx in range(3):
        for dy in range(3):
            tmp = cut(paper, x+dx*divide, y+dy*divide, divide, count)
            if tmp == -1 or tmp == 0 or tmp == 1:
                nums.append(tmp)
    if nums == [-1]*9 or nums == [0]*9 or nums == [1]*9:
        count[nums[0]+1] -= 8
        return nums[0]

main()
