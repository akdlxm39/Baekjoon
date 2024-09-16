import sys
input = sys.stdin.readline
num_dict = dict(zip('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(36)))
Bnum, B = input().split()
B = int(B)
answer = 0
for i, x in enumerate(Bnum[::-1]):
    answer += num_dict[x] * (B ** i)
print(answer)