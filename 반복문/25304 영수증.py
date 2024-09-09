X = int(input())
N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    X -= A * B
print("No" if X else "Yes")