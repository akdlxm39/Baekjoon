import sys
input = sys.stdin.readline

def dfs(board, papers, pos, can, check, cur, ans):
    if cur > ans[0]:
        return
    i = 0
    x, y = 0, 0
    while board[x][y] == 0 or check[x][y]:
        if i == len(pos):
            if cur < ans[0]:
                ans[0] = cur
            return
        x, y = pos[i]
        i += 1
    for size in range(min(can[x][y], 5), 0, -1):
        if papers[size]:
            papers[size] -= 1
            check_update(check, x, y, size, 1)
            dfs(board, papers, pos, can, check, cur+1, ans)
            check_update(check, x, y, size, 0)
            papers[size] += 1
    return

def check_update(check, x, y, size, boolean):
    for i in range(x, x+size):
        for j in range(y, y+size):
            check[i][j] = boolean

def check_size(board, x, y):
    res = 10
    cnt = 0
    for i in range(x, 10):
        if board[i][y] == 0:
            break
        tmp = 1
        for j in range(y+1, 10):
            if board[i][j] == 0:
                break
            tmp += 1
        if tmp < cnt:
            break
        res = min(res, tmp)
        cnt += 1
    return min(cnt, res)

def main():
    papers = [0, 5, 5, 5, 5, 5]
    board = [list(map(int, input().split())) for _ in range(10)]
    pos = [(i, j) for i in range(10) for j in range(10) if board[i][j]]
    can = [[check_size(board, i, j) for j in range(10)] for i in range(10)]
    check = [[0]*10 for _ in range(10)]
    ans = [1000000]
    print()
    for b in can:
        print(*b)
    dfs(board, papers, pos, can, check, 0, ans)
    print(ans[0] if ans[0] != 1000000 else -1)


if __name__ == "__main__":
    main()