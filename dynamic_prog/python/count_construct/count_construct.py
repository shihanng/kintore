def count_construct(target, words, memo={}) -> int:
    val = memo.get(target)
    if val is not None:
        return val

    if target == "":
        return 1

    total = 0
    for word in words:
        if target.startswith(word):
            c = count_construct(target[len(word) :], words, memo)

            if c:
                total += c

    memo[target] = total
    return total


def count_construct_tab(target, words):
    tab = [0] * (len(target) + 1)
    tab[0] = 1

    for i, _ in enumerate(target):
        if tab[i] == 0:
            continue

        for word in words:
            if not target[i:].startswith(word):
                continue

            n = i + len(word)
            if n < len(tab):
                tab[n] += tab[i]

    return tab[-1]
