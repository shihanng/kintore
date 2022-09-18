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
