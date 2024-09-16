import sys
input = sys.stdin.readline
X = [input().rstrip() for _ in range(5)]
Y = ''.join(row[col] for col in range(15) for row in X if col < len(row))
print(Y)