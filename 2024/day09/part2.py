with open('input.txt', 'r', encoding='utf-8') as f:
    partitioning: list[tuple[int|None, int]] = []

    pid = 0
    free = False
    for c in f.read().strip():
        partitioning.append((pid if not free else None, int(c)))
        free = not free
        pid += free

    for i in range(len(partitioning) - 1, -1, -1):
        pi, li = partitioning[i]
        if pi is None:
            continue
        for j in range(i):
            pj, lj = partitioning[j]
            if pj is not None:
                continue
            if lj >= li:
                l = lj - li
                partitioning[j] = (pi, li)
                if partitioning[i - 1][0] is None:
                    li += partitioning[i - 1][1]
                    partitioning[i - 1] = (None, 0)
                if i >= len(partitioning) and partitioning[i + 1][0] is None:
                    li += partitioning[i + 1][1]
                    partitioning[i + 1] = (None, 0)
                partitioning[i] = (None, li)
                if l > 0:
                    partitioning.insert(j + 1, (None, l))
                break

    count = 0
    idx = 0
    for pi, li in partitioning:
        if pi is not None:
            for i in range(li):
                count += (idx + i) * pi
        idx += li

    print(count)

