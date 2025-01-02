mod = 10**9 + 7
n = int(input())
grid = [input() for i in range(n)]
dp = [[0] * n for i in range(n)]
dp[0][0] = 1 if grid[0][0] == "." else 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != "*":
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= mod
print(dp[n - 1][n - 1])
