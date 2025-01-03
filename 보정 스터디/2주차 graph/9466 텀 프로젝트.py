import sys
input = sys.stdin.readline

def solve(l, visited, cur):
    circle = [cur]
    visited[cur] = True
    while True:
        wish = l[circle[-1]]
        if not visited[wish]:
            circle.append(wish)
            visited[wish] = True
            continue
        if wish in circle:
            return circle.index(wish)
        else:
            return len(circle)

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        l = [0] + list(map(int, input().split()))
        visited = [False]*(n+1)
        answer = 0
        for i in range(n+1):
            if visited[i]:
                continue
            answer += solve(l, visited, i)            
        print(answer)

if __name__ == "__main__":
    main()