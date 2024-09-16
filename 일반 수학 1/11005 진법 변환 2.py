import sys
from math import log, ceil
input = sys.stdin.readline
num_dict = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Intnum, B = map(int, input().split())
answer = ''
while Intnum > 0:
    Intnum, mod = divmod(Intnum, B)
    answer = num_dict[mod] + answer
print(answer)