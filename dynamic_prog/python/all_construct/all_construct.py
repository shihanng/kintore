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
