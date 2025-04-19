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


n, q = map(int, input().split())
ft = FenwickTree([*map(int, input().split())])
for _ in range(q):
    i, x, y = map(int, input().split())
    if i == 2:
        print(ft.query(y) - ft.query(x - 1))
    else:
        z = ft.query(x) - ft.query(x - 1)
        ft.update(x - 1, y - z)
