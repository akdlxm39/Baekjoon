import sys
input = sys.stdin.readline
from collections import Counter
N, M = map(int, input().split())
words = []
for _ in range(N):
    W = input().rstrip()
    if len(W) >= M:
        words.append(W)
words = sorted(Counter(words).items(), key=lambda w: (-w[1],-len(w[0]),w[0]))
print('\n'.join(word for word, _ in words))