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
