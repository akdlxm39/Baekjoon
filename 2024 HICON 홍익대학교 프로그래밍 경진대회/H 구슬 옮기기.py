import sys
input = sys.stdin.readline

W, H = map(int, input().split())
old = [list(map(int,input().split())) for _ in range(H)]
new = [list(map(int,input().split())) for _ in range(H)]
old_cnt = 0
new_cnt = 0
for x, y in zip(old, new):
    old_cnt += x.count(1)
    new_cnt += y.count(1)
if old_cnt == new_cnt:
    answer = 0
    for l in range(W+H):
        for d in range(l+1):
            i, j = l-d, d
            if not 0<=i<W or not 0<=j<H:
                continue
            if new[j][i]==0:
                continue
            if old[j][i] == 1:
                new[j][i] = 0
                old[j][i] = 0
                new_cnt -= 1
                continue
            for di,dj in [(0,-1),(-1,0),(1,0),(0,1)]:
                if 0<=i+di<W and 0<=j+dj<H:
                    if old[j+dj][i+di] == 1:
                        new[j][i] = 0
                        old[j+dj][i+di] = 0
                        answer += 1
                        new_cnt -= 1
                        break
    answer += 2*new_cnt
    print(answer)
else:
    print(-1)

