import sys
input = sys.stdin.readline

def main():
    exp = [sum(map(int, x.split('+'))) for x in input().split('-')]
    answer = 2 * exp[0] - sum(exp)
    print(answer)

main()