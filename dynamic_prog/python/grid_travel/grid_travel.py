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
