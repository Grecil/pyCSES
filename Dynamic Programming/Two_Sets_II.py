mod = 10**9 + 7
n = int(input())
if n % 4 in (0, 3):
    x = (n * (n + 1)) // 4
    dp = [1] + [0] * x
    for i in range(1, n + 1):
        for j in range(x - i, -1, -1):
            dp[j + i] = (dp[j + i] + dp[j]) % mod
    print((dp[x] * pow(2, mod - 2, mod)) % mod)
else:
    print(0)
