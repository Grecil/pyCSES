n = int(input())
grid = "".join(input() for i in range(n))
ans = [grid[0]]
arr = set([0])
for k in range(2 * n - 2):
    new, mn = set(), "Z"
    for x in arr:
        if x // n < n - 1:
            char = grid[x + n]
            if char < mn:
                mn = char
                new = set([x + n])
            elif char == mn:
                new.add(x + n)
        if x % n < n - 1:
            char = grid[x + 1]
            if char < mn:
                mn = char
                new = set([x + 1])
            elif char == mn:
                new.add(x + 1)
    arr = new
    ans.append(mn)
print("".join(ans))
