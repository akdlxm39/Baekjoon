import sys
input = sys.stdin.readline

def hanoi(N, s, m, d):
    if N == 1:
        print(s, d)
        return
    hanoi(N-1, s, d, m)
    print(s, d)
    hanoi(N-1, m, s, d)

def main():
    N = int(input())
    print(2 ** N -1)
    hanoi(N, 1, 2, 3)
main()