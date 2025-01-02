n, x = map(int, input().split())
c = list(map(int, input().split()))
ans = [1] + [0] * (10**7)
for i in range(x):
    for j in c:
        ans[i + j] = (ans[i + j] + ans[i]) % 1000000007
print(ans[x])
