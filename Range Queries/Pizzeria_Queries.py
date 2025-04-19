import sys


class SegmentTree:
    def __init__(self, data, default=int(1e18), func=min):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size : _size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


inp = sys.stdin.read().splitlines()
n, q = map(int, inp[0].split())
arr = [*map(int, inp[1].split())]
st1 = SegmentTree([i + arr[i] for i in range(n)])
st2 = SegmentTree([n - i - 1 + arr[i] for i in range(n)])
for line in inp[2:]:
    t = [*map(int, line.split())]
    if t[0] == 1:
        st1[t[1] - 1] = t[1] + t[2] - 1
        st2[t[1] - 1] = n + t[2] - t[1]
    else:
        ans1 = st1.query(t[1] - 1, n + 1) - t[1] + 1
        ans2 = st2.query(0, t[1]) - n + t[1]
        print(min(ans1, ans2))
