import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    nums = map(int, input().split())
    prefixsum = [1] + [0] * (M-1)
    tmp = 0
    answer = 0
    for num in nums:
        tmp = (tmp + num) % M
        answer += prefixsum[tmp]
        prefixsum[tmp] += 1
    print(answer)

main()