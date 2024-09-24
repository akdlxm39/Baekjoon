import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = input().rstrip()
    newS = []
    subS = ''
    for c in S:
        if c in 'aeiou':
            newS.append(subS)
            newS.append(c)
            subS = ''
        else:
            subS += c
    newS.append(subS)
    if len(newS) == 1 and newS[0] not in 'aeiou':
        print(-1)
        continue
    answer = 1
    for subS in newS[1:-1]:
        if subS in 'aeiou':
            continue
        answer = (answer * (len(subS)+1)) % 1000000007
    print(answer)
