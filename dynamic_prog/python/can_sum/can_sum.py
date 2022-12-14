def can_sum_memo(target, numbers, memo={}):
    val = memo.get(target)

    if val is not None:
        return val

    if target <= 0:
        return target == 0

    for number in numbers:
        new_target = target - number
        if can_sum_memo(new_target, numbers, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False


def can_sum_tab(target, numbers):
    tab = [False] * (target + 1)
    tab[0] = True

    for i, val in enumerate(tab):
        if not val:
            continue

        for n in numbers:
            m = i + n
            if m < len(tab):
                tab[m] = True

    return tab[-1]
