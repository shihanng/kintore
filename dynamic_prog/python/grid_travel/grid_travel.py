def grid_travel(m, n, memo={}):
    key = gen_key(m, n)
    c = memo.get(key)

    if c:
        return c

    if m == 0 or n == 0:
        return 0

    if m == 1 and n == 1:
        return 1

    n = grid_travel(m - 1, n) + grid_travel(m, n - 1)

    memo[key] = n
    return n


def gen_key(m, n):
    if m > n:
        return f"{n}-{m}"
    else:
        return f"{m}-{n}"


def grid_travel_tab(m, n) -> int:
    grid = [[0] * (n + 1) for _ in range(m + 1)]
    grid[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            try:
                grid[i][j + 1] += grid[i][j]
            except IndexError:
                pass

            try:
                grid[i + 1][j] += grid[i][j]
            except IndexError:
                pass

    return grid[m][n]
