import sys
input = sys.stdin.readline

def solve(matrix, size, x, y):
    if size == 2:
        return sorted([matrix[x][y], matrix[x][y+1],
                       matrix[x+1][y], matrix[x+1][y+1]])[2]
    new_size = size//2
    return sorted([solve(matrix, new_size, x, y),
                   solve(matrix, new_size, x, y+new_size),
                   solve(matrix, new_size, x+new_size, y),
                   solve(matrix, new_size, x+new_size, y+new_size)])[2]

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(solve(matrix, n, 0, 0))

if __name__ == "__main__":
    main()