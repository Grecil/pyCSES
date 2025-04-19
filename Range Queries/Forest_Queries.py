from itertools import accumulate

n, q = map(int, input().split())
dp = [[0] * (n + 1)]
for i in range(n):
    dp.append(
        [i + j for i, j in zip(dp[-1], [0, *accumulate(i == "*" for i in input())])]
    )
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])
