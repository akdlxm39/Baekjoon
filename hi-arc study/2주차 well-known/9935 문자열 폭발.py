import sys
input = sys.stdin.readline

def main():
    s = input().rstrip()
    bomb = list(input().rstrip())
    bomb_len, catalyst = len(bomb), bomb[-1]
    stack = []
    for c in s:
        stack.append(c)
        if c == catalyst and stack[-bomb_len:] == bomb:
            del stack[-bomb_len:]
    print(''.join(stack) if stack else "FRULA")

if __name__ == "__main__":
    main()