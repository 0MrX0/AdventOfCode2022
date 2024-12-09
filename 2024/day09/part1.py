with open('input.txt', 'r', encoding='utf-8') as f:
    partitioning: list[int|None] = []

    pid = 0
    free = False
    for c in f.read().strip():
        for i in range(int(c)):
            partitioning.append(pid if not free else None)
        free = not free
        pid += free

    free_idx = 0
    for i in range(len(partitioning) - 1, -1, -1):
        if partitioning[i] is None:
            continue
        while partitioning[free_idx] is not None:
            free_idx += 1
        if i < free_idx:
            break
        partitioning[free_idx], partitioning[i] = partitioning[i], None

    print(sum(idx * p for idx, p in enumerate(partitioning) if p is not None))
