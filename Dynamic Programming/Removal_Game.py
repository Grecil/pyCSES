n = int(input())
arr = [int(i) for i in input().split()]
dp = arr.copy()
for d in range(1, n):
    for i in range(n - d):
        dp[i] = max(arr[i] - dp[i + 1], arr[i + d] - dp[i])
print((sum(arr) + dp[0]) // 2)
