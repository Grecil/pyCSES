a, b = sorted((input(), input()), key=len)
n, m = len(a), len(b)
dp = list(range(n + 1))
for i in range(1, m + 1):
    x, dp[0] = dp[0], i
    for j in range(1, n + 1):
        dp[j], x = min(x + int(a[j - 1] != b[i - 1]), dp[j - 1] + 1, dp[j] + 1), dp[j]
print(dp[n])
