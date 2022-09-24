def best_sum(target, numbers, memo={}):
    val = memo.get(target, -1)

    if val != -1:
        return val

    if target == 0:
        return []

    if target < 0:
        return None

    best = None
    for number in numbers:
        new_target = target - number

        res = best_sum(new_target, numbers, memo)
        if res is None:
            continue

        if best is None or len(res) < len(best):
            best = [*res, number]

    memo[target] = best
    return best


def best_sum_tab(target, numbers):
    tab = [None] * (target + 1)
    tab[0] = []

    for i, col in enumerate(tab):
        if col is None:
            continue

        for num in numbers:
            n = i + num

            if n >= len(tab):
                continue

            if tab[n] is None or len(tab[n]) > len([*col, num]):
                tab[n] = [*col, num]

    return tab[-1]
