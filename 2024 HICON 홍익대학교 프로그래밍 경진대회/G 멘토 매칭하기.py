import sys
from itertools import zip_longest
from math import factorial as fact
input = sys.stdin.readline




N, M = map(int, input().split())
mente = sorted(map(int, input().split()))
mento = sorted(map(int, input().split()), reverse=True)
print(mente)
print(mento)
maximum = max(a+b for a, b in zip_longest(mente, mento, fillvalue=0))

def match(mente_idx, mento_num, mento_used):
    if mente_idx == N:
        return 1
    if mente[mente_idx] >= maximum:
        return (fact(N-mente_idx+mento_num)//fact(mento_num))%1000000007
    result = 0
    for i in range(M):
        if mento_used[i]:
            continue
        if mente[mente_idx] + mento[i] < maximum:
            break
        mento_used[i] = True
        result += match(mente_idx+1, mento_num-1, mento_used)
        mento_used[i] = False