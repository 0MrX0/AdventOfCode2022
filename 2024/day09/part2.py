with open('input.txt', 'r', encoding='utf-8') as f:
    partitioning = []

    pid = 0
    free = False
    for c in f.read().strip():
        for i in range(int(c)):
            if free:
                partitioning.append(None)
            else:
                partitioning.append(pid)
        free = not free
        if free:
            pid += 1

    free_idx = 0
    for i in range(len(partitioning) - 1, -1, -1):
        if free_idx >= len(partitioning):
            break
        if partitioning[i] is None:
            continue
        while partitioning[free_idx] is not None:
            free_idx += 1
        if i < free_idx:
            break
        partitioning[free_idx], partitioning[i] = partitioning[i], None

    checksum = sum([idx * p for idx, p in enumerate(partitioning) if p is not None])

    print(checksum)