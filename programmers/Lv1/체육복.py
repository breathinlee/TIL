def solution(n, lost, reserve):
    onlyreserve = set(reserve) - set(lost)
    onlylost = set(lost) - set(reserve)

    for r in onlyreserve:
        one = r - 1
        two = r + 1

        if one in onlylost:
            onlylost.remove(one)
        elif two in onlylost:
            onlylost.remove(two)

    return n - len(onlylost)