import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    coins = sorted((int(input()) for _ in range(N)), reverse=True)
    answer = 0
    for coin in coins:
        if K == 0:
            break
        if coin > K:
            continue
        answer += K // coin
        K %= coin
    print(answer)

main()