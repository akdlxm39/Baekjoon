import sys
input = sys.stdin.readline

def nostar(s):
    if len(s)%2:
        return False
    half = len(s)//2 - s.count('(')
    cnt = 0
    for i, c in enumerate(s):
        if c == '(':
            cnt += 1
        elif c == '?' and half > 0:
            cnt += 1
            half -= 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True if cnt == 0 else False

def star(s, x):
    cnt = 0
    for c in s:
        if c == x or c == '?':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True

def main():
    for _ in range(int(input())):
        s = input().rstrip().split('*')
        if len(s) == 1 and nostar(s[0]):
            print("YES")
        elif len(s) >= 2 and star(s[0], '(') and star(reversed(s[-1]), ')'):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()