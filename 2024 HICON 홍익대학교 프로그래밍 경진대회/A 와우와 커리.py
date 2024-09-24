import sys
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    S = input().rstrip()
    count = 0
    for i in range(len(S)-2):
        if S[i:i+3] == 'WOW':
            count += 1
    print(count)