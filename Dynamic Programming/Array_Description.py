mod = 10**9 + 7
n, m = map(int, input().split())
x = [int(i) for i in input().split()]
dp = [[0] * m for i in range(n)]
for i in range(n):
    if not x[i]:
        if not i:
            dp[i] = [1] * m
        else:
            dp[i][0] = sum(dp[i - 1][:2]) % mod
            for j in range(1, m):
                dp[i][j] = dp[i][j - 1]
                if j > 1:
                    dp[i][j] -= dp[i - 1][j - 2]
                if j < m - 1:
                    dp[i][j] += dp[i - 1][j + 1]
                dp[i][j] %= mod
    else:
        if not i:
            dp[i][x[i] - 1] = 1
        else:
            dp[i][x[i] - 1] = sum(dp[i - 1][max(0, x[i] - 2) : min(x[i] + 1, m)]) % mod
ans = 0
for i in dp[n - 1]:
    ans = (ans + i) % mod
print(ans)
