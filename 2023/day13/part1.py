with open('input.txt', 'r', encoding='utf-8') as f:
    patterns = [[[x == '#' for x in y if x] for y in z.split('\n') if y] for z in ''.join(f.readlines()).split('\n\n')]

    res = 0

    for pattern in patterns:
        for x, pat in enumerate([pattern, list(zip(*pattern))]):
            for i, (row, row2) in enumerate(zip(pat, pat[1:])):
                if row != row2:
                    continue
                equal = True
                j = 0
                while i - j >= 0 and i + j + 1 < len(pat):
                    if pat[i - j] != pat[i + j + 1]:
                        equal = False
                        break
                    j += 1
                if equal:
                    if x:
                        res += i + 1
                    else:
                        res += (i + 1) * 100
    print(res)
