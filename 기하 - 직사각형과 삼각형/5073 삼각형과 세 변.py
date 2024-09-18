import sys
input = sys.stdin.readline
while True:
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break
    if A + B + C - 2 * max(A, B, C) <= 0:
        print("Invalid")
    elif A == B and B == C:
        print("Equilateral")
    elif A == B or B == C or C == A:
        print("Isosceles")
    else:
        print("Scalene")