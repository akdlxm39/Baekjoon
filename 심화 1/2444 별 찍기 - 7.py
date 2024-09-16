import sys
input = sys.stdin.readline
N = int(input())
for i in range(2 * N - 1):
    print(f"{' ' * abs(N-1-i)}{'*' * (1 + 2 * (N - 1 - abs(N-1-i)))}")