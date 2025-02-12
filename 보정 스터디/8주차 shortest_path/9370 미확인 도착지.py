import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

def main():
    for _ in range(int(input())):
        n, m, t = map(int, input().split())
        s, g, h = map(int, input().split())
        adj = [[]  for _ in range(n+1)]
        dists = [INF] * (n+1)
        smelled = [False] * (n+1)
        heap = [(0, s, s)]
        for _ in range(m):
            a, b, d = map(int, input().split())
            adj[a].append((d, b))
            adj[b].append((d, a))
        x_list = sorted(int(input()) for _ in range(t))
        while heap:
            cur_dist, prev, cur = heappop(heap)
            # print(prev, cur, cur_dist, chk)
            if dists[cur] != INF:
                continue
            dists[cur] = cur_dist
            if smelled[prev] or (prev == g and cur == h) or (prev == h and cur == g):
                smelled[cur] = True
            for d, nxt in adj[cur]:
                if dists[nxt] != INF:
                    continue
                heappush(heap, (cur_dist+d, cur, nxt))
        print(*[x for x in x_list if smelled[x]])

if __name__ == "__main__":
    main()