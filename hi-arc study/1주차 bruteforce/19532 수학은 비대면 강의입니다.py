import sys
input = sys.stdin.readline

def main():
    a, b, c, d, e, f = map(int, input().split())
    x = (c*e - b*f) // (a*e - b*d)
    y = ((c - a * x) // b) if b else (f - d * x) // e
    print(x, y)

if __name__ == "__main__":
    main()