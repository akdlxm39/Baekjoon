import sys
input = sys.stdin.readline
from collections import Counter
S = input().rstrip().upper()
C = Counter(S).most_common()
print(C[0][0] if len(C) == 1 or C[0][1] != C[1][1] else '?')