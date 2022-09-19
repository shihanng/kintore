def fib(n: int):
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


def fib_memo(n: int, memo={}):
    val = memo.get(n)
    if val:
        return val

    if n <= 2:
        return 1

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_tab(n: int):
    tab = [0] * (n + 1)
    tab[1] = 1

    for i in range(n + 1):
        if i + 1 <= n:
            tab[i + 1] += tab[i]
        if i + 2 <= n:
            tab[i + 2] += tab[i]

    return tab[n]
