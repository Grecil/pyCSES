mod = 10**9 + 7
n = int(input())
curr = [2**i for i in range(6)]
if n > 6:
    x = sum(curr)
    for i in range(6, n):
        x %= mod
        curr.append(x)
        x -= curr[i - 6]
        x += curr[i]
print(curr[n - 1])
