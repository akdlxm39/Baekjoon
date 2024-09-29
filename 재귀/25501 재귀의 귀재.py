import sys
input = sys.stdin.readline

def palindrome(s, l, r, cnt):
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    return palindrome(s, l+1, r-1, cnt+1)

def main():
    T = int(input())
    for _ in range(T):
        S = input().rstrip()
        print(*palindrome(S, 0, len(S)-1, 1))

main()