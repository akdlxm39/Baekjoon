H, M = map(int, input().split())
T = int(input())
print((H + (M + T) // 60) % 24, (M + T) % 60)