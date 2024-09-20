import sys
input = sys.stdin.readline
N = int(input())
cards = dict()
for card in map(int, input().split()):
    if card in cards:
        cards[card] += 1
    else:
        cards[card] = 1
M = int(input())
doHave = [cards[card] if card in cards else 0 for card in map(int,input().split())]
print(*doHave)