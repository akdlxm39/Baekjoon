import sys
input = sys.stdin.readline

while True:
    S = input().rstrip()
    if S == '.':
        break
    stack = []
    for c in S:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if not stack or stack.pop() != 1:
                print("no")
                break
        elif c == '[':
            stack.append(2)
        elif c == ']':
            if not stack or stack.pop() != 2:
                print("no")
                break
        elif c == '.':
            if stack:
                print("no")
                break
    else:
        print("yes")