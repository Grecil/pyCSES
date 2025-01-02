n = int(input())
ans = 0
while n > 0:
    n -= int(max(str(n)))
    ans += 1
print(ans)
