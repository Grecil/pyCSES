mod = 1000000007
n = int(input())
arr = [int(input()) for i in range(n)]
x = max(arr)
dp = [[0] * 2 for i in range(x)]
dp[0] = [1] * 2
for i in range(1, x):
    dp[i][0] = (dp[i - 1][0] * 4 + dp[i - 1][1]) % mod
    dp[i][1] = (dp[i - 1][1] * 2 + dp[i - 1][0]) % mod
print(*[sum(dp[i - 1]) % mod for i in arr], sep="\n")
