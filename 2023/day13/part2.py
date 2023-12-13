with open('input.txt', 'r', encoding='utf-8') as f:
    patterns = [[[x == '#' for x in y if x] for y in z.split('\n') if y] for z in ''.join(f.readlines()).split('\n\n')]

    res = 0

    for pattern in patterns:
        for x, pat in enumerate([pattern, list(zip(*pattern))]):
            for i, (_, _) in enumerate(zip(pat, pat[1:])):
                diff = 0
                j = 0
                while i - j >= 0 and i + j + 1 < len(pat) and diff <= 1:
                    diff += len([1 for x, y in zip(pat[i - j], pat[i + j + 1]) if x != y])
                    j += 1
                if diff == 1:
                    if x:
                        res += i + 1
                    else:
                        res += (i + 1) * 100
                    break
    print(res)
