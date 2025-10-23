from functools import lru_cache


@lru_cache(None)
def dp(i, prev, leading, tight):
    if i == 20:
        return 1
    ans = 0
    ub = lim[i] if tight else 9
    for j in range(ub + 1):
        if j != prev or (j == 0 and leading):
            ans += dp(i + 1, j, leading & (j == 0), tight & (j == ub))
    return ans


a, b = map(int, input().split())
ta, tb = a, b
lim = []
for i in range(20):
    lim.append(ta % 10)
    ta //= 10
lim.reverse()
num1 = dp(0, -1, True, True)
dp.cache_clear()
lim = []
for i in range(20):
    lim.append(tb % 10)
    tb //= 10
lim.reverse()
num2 = dp(0, -1, True, True)
sa = str(a)
print(num2 - num1 + all(sa[i] != sa[i + 1] for i in range(len(sa) - 1)))
