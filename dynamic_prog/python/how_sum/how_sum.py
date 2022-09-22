def how_sum(target, numbers, memo={}):
    val = memo.get(target, -1)
    if val != -1:
        return val

    if target == 0:
        return []

    if target < 0:
        return None

    for number in numbers:
        how = how_sum(target - number, numbers, memo)
        if how is not None:
            memo[target] = [*how, number]
            return memo[target]

    memo[target] = None
    return None


def how_sum_tab(target, numbers):
    tab = [None] * (target + 1)
    tab[0] = []

    for i, col in enumerate(tab):
        if col is None:
            continue

        for num in numbers:
            n = i + num

            if n < len(tab):
                tab[n] = [*col, num]

    return tab[-1]
