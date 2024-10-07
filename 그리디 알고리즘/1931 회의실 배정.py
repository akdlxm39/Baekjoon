import sys
input = sys.stdin.readline

def main():
    N = int(input())
    meetings = sorted((tuple(map(int, input().split())) for _ in range(N)), key=lambda x:(x[1],x[0]))
    time = 0
    answer = 0
    for s, e in meetings:
        if s < time:
            continue
        answer += 1
        time = e
    print(answer)

main()