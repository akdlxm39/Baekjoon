import sys
input = sys.stdin.readline
chess = [1, 1, 2, 2, 2, 8]
I = list(map(int, input().split()))
O = [chess[i] - I[i] for i in range(6)]
print(*O)