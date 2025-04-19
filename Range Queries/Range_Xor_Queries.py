class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] ^= x[i]

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x ^= self.bit[end - 1]
            end &= end - 1
        return x


n, q = map(int, input().split())
ft = FenwickTree([*map(int, input().split())])
for _ in range(q):
    x, y = map(int, input().split())
    print(ft.query(y) ^ ft.query(x - 1))
