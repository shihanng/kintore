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
