a, b = sorted(map(int, input().split()))
dp = [[float("inf")] * b for _ in range(a)]
for i in range(a):
    dp[i][i] = 0
for i in range(b):
    dp[0][i] = i
    dp[i % a][0] = i % a
for i in range(1, a):
    for j in range(i + 1, b):
        mn1 = min(dp[i][k] + dp[i][j - k - 1] for k in range(j // 2 + 1))
        mn2 = min(dp[k][j] + dp[i - k - 1][j] for k in range(i // 2 + 1))
        dp[i][j] = min(mn1, mn2) + 1
        if j < a:
            dp[j][i] = dp[i][j]
print(dp[a - 1][b - 1])
# print(dp)
