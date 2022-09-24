def can_construct(target, words, memo={}) -> bool:
    val = memo.get(target)
    if val is not None:
        return val

    if target == "":
        return True

    for word in words:
        if target.startswith(word):
            if can_construct(target[len(word) :], words, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


def can_construct_tab(target, words):
    tab = [False] * (len(target) + 1)
    tab[0] = True

    for i, _ in enumerate(target):
        if not tab[i]:
            continue

        for word in words:
            if not target[i:].startswith(word):
                continue

            n = i + len(word)
            if n < len(tab):
                tab[n] = True

    return tab[-1]
