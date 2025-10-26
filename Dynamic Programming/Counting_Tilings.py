mod = int(1e9 + 7)
n, m = map(int, input().split())
dp = [[0] * (1 << n) for i in range(n + 1)]
dp[0][0] = 1
for i in range(m):
    for j in range(n):
        for k in range(1 << n):
            dp[j][k] %= mod
            if k & (1 << j):
                dp[j + 1][k ^ (1 << j)] += dp[j][k]
            else:
                dp[j + 1][k | (1 << j)] += dp[j][k]
                if j + 1 < n and not k & (1 << (j + 1)):
                    dp[j + 2][k] += dp[j][k]
    dp = [dp[-1]] + [[0] * (1 << n) for i in range(n)]
print(dp[0][0] % mod)
