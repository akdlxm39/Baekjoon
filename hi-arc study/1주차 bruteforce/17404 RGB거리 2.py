import sys
input = sys.stdin.readline

def main():
    n = int(input())
    r, g, b = map(int, input().split())
    roof = [r, 10000, 10000, 10000, g, 10000, 10000, 10000, b]
    for _ in range(n-1):
        color = tuple(map(int, input().split()))
        next_roof = roof[:]
        for i in range(0, 9, 3):
            for j in range(3):
                next_roof[i+j] = color[j] + min(roof[i+(j+1)%3], roof[i+(j+2)%3])
        roof = next_roof
    print(min(roof[1:4]+roof[5:8]))

if __name__ == "__main__":
    main()