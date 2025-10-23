from functools import lru_cache


def nums_till(x):
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

    lim = []
    for i in range(20):
        lim.append(x % 10)
        x //= 10
    lim.reverse()
    return dp(0, -1, True, True)


a, b = input().split()
print(nums_till(int(b)) - nums_till(int(a)) + all(a[i] != a[i + 1] for i in range(len(a) - 1)))
