import sys
input = sys.stdin.readline

def sudoku(board, blank, check, idx):
    if idx == len(blank):
        return True
    x, y = blank[idx]
    for i in range(1, 10):
        if check[0][x][i] or check[1][y][i] or check[2][(x//3)*3+y//3][i]:
            continue
        check[0][x][i] = check[1][y][i] = check[2][(x//3)*3+y//3][i] = True
        board[x][y] = i
        if sudoku(board, blank, check, idx+1):
            return True
        check[0][x][i] = check[1][y][i] = check[2][(x//3)*3+y//3][i] = False
        board[x][y] = 0
    return False

def main():
    board = [list(map(int, input().split())) for _ in range(9)]
    blank = []
    check = [[[False]*10 for _ in range(9)], [[False]*10 for _ in range(9)], [[False]*10 for _ in range(9)]]
    for x, line in enumerate(board):
        for y, a in enumerate(line):
            if board[x][y] == 0:
                blank.append((x, y))
                continue
            check[0][x][a] = True
            check[1][y][a] = True
            check[2][(x//3)*3 + y//3][a] = True
    sudoku(board, blank, check, 0)
    print('\n'.join(' '.join(map(str, line)) for line in board))

main()