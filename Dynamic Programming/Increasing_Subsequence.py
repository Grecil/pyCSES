from bisect import bisect_right as bsr

n = int(input())
arr = [int(i) for i in input().split()]
dp = [float("-inf")] + [float("inf")] * (n + 1)
for i in range(n):
    x = bsr(dp, arr[i])
    if dp[x - 1] < arr[i] < dp[x]:
        dp[x] = arr[i]
print(dp.index(float("inf")) - 1)
