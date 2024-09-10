import sys
input = sys.stdin.readline
max, idx = 0, 0
for i in range(1, 10):
    x = int(input())
    if x > max:
        max = x
        idx = i
print(f"{max}\n{idx}")