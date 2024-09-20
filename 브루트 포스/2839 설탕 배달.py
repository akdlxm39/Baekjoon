import sys
input = sys.stdin.readline
N = int(input())
answer = 5000
for x in range(N//5, -1, -1):
    if (N - 5 * x) % 3 == 0:
        answer = x + (N - 5 * x) // 3
        break
else:
    answer = -1
print(answer)