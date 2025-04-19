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
arr = [*map(int, input().split())]
ft = FenwickTree([arr[0], *(arr[i + 1] - arr[i] for i in range(n - 1))])
for _ in range(q):
    i, *x = map(int, input().split())
    if i == 2:
        print(ft.query(x[0]))
    else:
        ft.update(x[0] - 1, x[2])
        ft.update(x[1], -x[2])
