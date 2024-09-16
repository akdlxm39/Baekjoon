import sys
input = sys.stdin.readline
coin_dict = [25, 10, 5, 1]
T = int(input())
for _ in range(T):
    change = int(input())
    answer = []
    for c in coin_dict:
        answer.append(change//c)
        change %= c
    print(*answer)