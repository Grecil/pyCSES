from functools import lru_cache


@lru_cache(None)
def ways(n):
    if n == 0:
        return 0
    if arr[n - 1] != -1:
        return arr[n - 1]
    mn = float("inf")
    for i in str(n):
        if n - int(i) >= 0 and int(i):
            temp = ways(n - int(i))
            mn = min(mn, temp)
    arr[n - 1] = mn + 1
    return mn + 1


n = int(input())
arr = [-1] * n
print(ways(n))

# Greedy Solution

# n = int(input())
# ans = 0
# while n > 0:
#     n -= int(max(str(n)))
#     ans += 1
# print(ans)
