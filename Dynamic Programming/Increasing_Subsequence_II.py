mod = int(1e9 + 7)


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
            self.bit[idx] = (self.bit[idx] + x) % mod
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x = (x + self.bit[end - 1]) % mod
            end &= end - 1
        return x


n = int(input())
arr = [*map(int, input().split())]
v2i = {v: i for i, v in enumerate(sorted(set(arr)))}
ft = FenwickTree([0] * len(v2i))
ans = 0
for v in arr:
    x = ft.query(v2i[v]) + 1
    ft.update(v2i[v], x)
    ans = (ans + x) % mod
print(ans)
