import sys
input = sys.stdin.readline

def main():
    N = int(input())
    roads = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    answer = 0
    mincost = 1000000000
    for i in range(N-1):
        if costs[i] < mincost:
            mincost = costs[i]
        answer += mincost * roads[i]
    print(answer)

main()