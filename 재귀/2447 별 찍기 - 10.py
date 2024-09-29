import sys
input = sys.stdin.readline

def star(N):
    if N == 1:
        return '*'
    next = N // 3
    tmp1 = star(next)
    tmp2 = [' ' * next for _ in range(next)]
    line1 = [x + y + z for x, y, z in zip(tmp1, tmp1, tmp1)]
    line2 = [x + y + z for x, y, z in zip(tmp1, tmp2, tmp1)]
    return line1 + line2 + line1

def main():
    N = int(input())
    stars = star(N)
    for line in stars:
        print(line)
main()