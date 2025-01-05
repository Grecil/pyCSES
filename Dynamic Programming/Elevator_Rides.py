n, x = map(int, input().split())
w = [int(i) for i in input().split()]
dp = [(float("inf"), float("inf")) for _ in range(1 << n)]
dp[0] = (1, 0)
for i in range(1, 1 << n):
    for j in range(n):
        if (1 << j) & i:
            a, b = dp[i ^ (1 << j)]
            flag = (b + w[j]) > x
            dp[i] = min(dp[i], (a + flag, w[j] + b * (1 - flag)))
print(dp[-1][0])
