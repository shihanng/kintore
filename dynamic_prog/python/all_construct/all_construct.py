from typing import Optional


def all_construct(target, words, memo={}) -> list[list[str]]:
    val = memo.get(target)
    if val is not None:
        return val

    if target == "":
        return [[]]

    all = []
    for word in words:
        if target.startswith(word):
            sub_all = all_construct(target[len(word) :], words, memo)

            for s in sub_all:
                all.append([word, *s])

    memo[target] = all
    return all


def all_construct_tab(target, words):
    tab: list[list[list[str]]] = [[]] * (len(target) + 1)
    tab[0] = [[]]

    for i, _ in enumerate(target):
        if len(tab[i]) == 0:
            continue

        for word in words:
            if not target[i:].startswith(word):
                continue

            n = i + len(word)
            if n < len(tab):
                for t in tab[i]:
                    tab[n] = [*tab[n], [*t, word]]

    return tab[-1]
