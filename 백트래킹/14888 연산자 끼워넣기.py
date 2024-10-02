import sys
input = sys.stdin.readline

def func2(cur, i, now):
    if i == 0:
        return cur + now
    elif i == 1:
        return cur - now
    elif i == 2:
        return cur * now
    elif cur >= 0:
        return cur // now
    else:
        return -(abs(cur) // now)

def func(N, nums, opers, idx, cur, M):
    if idx == N:
        M[0] = max(M[0], cur)
        M[1] = min(M[1], cur)
        return
    for i in range(4):
        if opers[i]:
            opers[i] -= 1
            func(N, nums, opers, idx+1, func2(cur, i, nums[idx]), M)
            opers[i] += 1

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    opers = list(map(int, input().split()))
    M = [-1000000000, 1000000000]
    func(N, nums, opers, 1, nums[0], M)
    print(M[0])
    print(M[1])
main()