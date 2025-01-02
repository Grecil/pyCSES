from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc


@bootstrap
def ways(n):
    if n == 0:
        yield 0
    if arr[n - 1] != -1:
        yield arr[n - 1]
    mn = float("inf")
    for i in str(n):
        if n - int(i) >= 0 and int(i):
            temp = yield ways(n - int(i))
            mn = min(mn, temp)
    arr[n - 1] = mn + 1
    yield mn + 1


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
