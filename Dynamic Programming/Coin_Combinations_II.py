n, x = map(int, input().split())
c = [int(i) for i in input().split()]
ans = [1] + [0] * (10**7)
for j in c:
    for i in range(x):
        ans[i + j] = (ans[i + j] + ans[i]) % 1000000007
print(ans[x])
