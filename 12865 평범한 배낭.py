n, k = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(k + 1)
for cur_w, cur_v in bag:
    for w in range(k, cur_w-1, -1):
        dp[w] = max(dp[w], dp[w-cur_w] + cur_v)
    print(dp)
print(dp[k])
