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
