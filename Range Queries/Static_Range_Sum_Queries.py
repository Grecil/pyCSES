from itertools import accumulate

n, q = map(int, input().split())
arr = [0, *accumulate(map(int, input().split()))]
for _ in range(q):
    x, y = map(int, input().split())
    print(arr[y] - arr[x - 1])
