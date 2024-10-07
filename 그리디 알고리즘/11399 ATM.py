import sys
input = sys.stdin.readline

def main():
    N = int(input())
    duration = sorted(map(int,input().split()))
    answer = 0
    for i, t in enumerate(duration):
        answer += (N-i) * t
    print(answer)

main()