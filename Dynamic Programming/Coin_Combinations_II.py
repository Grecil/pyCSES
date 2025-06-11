n, x = map(int, input().split())
c = list(map(int, input().split()))
ans = [1] + [0] * (10**7)
for j in c:
    for i in range(x):
        ans[i + j] = (ans[i + j] + ans[i]) % 1000000007
print(ans[x])
