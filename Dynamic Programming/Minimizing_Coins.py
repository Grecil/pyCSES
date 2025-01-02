n, x = map(int, input().split())
c = [int(i) for i in input().split()]
c.sort()
ans = [-1] * (x)
for i in range(x):
    if i + 1 in c:
        ans[i] = 1
        continue
    mn = float("inf")
    flag = False
    for j in range(n):
        if c[j] <= i:
            if ans[i - c[j]] > 0:
                mn = min(mn, ans[i - c[j]])
                flag = True
        else:
            break
    if flag:
        ans[i] = mn + 1
print(ans[x - 1])
