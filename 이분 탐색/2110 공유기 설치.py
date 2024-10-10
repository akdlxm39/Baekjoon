import sys
input = sys.stdin.readline

def main():
    N, C = map(int, input().split())
    houses = sorted(int(input()) for _ in range(N))
    answer = binary_search(houses, C)
    print(answer)

def binary_search(houses, N):
    l, r = 1, houses[-1]-houses[0]
    while l<=r:
        m = (l+r)//2
        if check(houses, m) >= N:
            l = m+1
        else:
            r = m-1
    return r

def check(houses, m):
    result = 1
    cur = houses[0]    
    for house in houses[1:]:
        if house >= cur + m:
            result += 1
            cur = house
    return result

main()