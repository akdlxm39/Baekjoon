import sys
input = sys.stdin.readline

def cantor_set(N):
    if N == 0:
        return '-'
    tmp = cantor_set(N-1)
    return tmp + ' ' * (3**(N-1)) + tmp

def main():
    while True:
        try:
            n = int(input())
        except:
            break
        print(cantor_set(n))
main()