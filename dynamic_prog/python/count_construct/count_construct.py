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
