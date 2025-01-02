n = int(input())
arr = [int(i) for i in input().split()]
dp = set([0])
for i in arr:
    dp |= set(j + i for j in dp)
print(len(dp) - 1)
print(*sorted(dp)[1:])
