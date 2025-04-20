import sys
from collections import defaultdict


class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1


inp = sys.stdin.read().splitlines()
n, q = map(int, inp[0].split())
arr = [*map(int, inp[1].split())]
ans = [0] * q
queries = []
for i in range(q):
    l, r = map(int, inp[2 + i].split())
    queries.append((l - 1, r - 1, i))
queries.sort()
d = defaultdict(list)
for i in range(n - 1, -1, -1):
    d[arr[i]].append(i)
f = [0] * n
for i in d:
    f[d[i].pop()] = 1
ft = FenwickTree(f)
prev = 0
for l, r, k in queries:
    for i in range(prev, l):
        if d[arr[i]]:
            ft.update(d[arr[i]].pop(), 1)
    prev = l
    ans[k] = str(ft.query(r + 1) - ft.query(l))
print("\n".join(ans))
