n, m = map(int, input().split())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if b[i - 1] == a[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[m][n])
lcs = []
i, j = m, n
while i > 0 and j > 0:
    if b[i - 1] == a[j - 1]:
        lcs.append(a[j - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1
print(*lcs[::-1])
