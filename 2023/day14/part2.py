with open('input.txt', 'r', encoding='utf-8') as f:
    dish = [[None if x == '.' else x == 'O' for x in l.strip()] for l in f if l.strip()]
    rounds = 1000000000
    cache = {}

    i = 0
    while i < rounds:
        hashable = tuple(map(tuple, dish))
        if hashable in cache:
            j, d2 = cache[hashable]
            if i + (i - j) > rounds:
                i += 1
                dish = d2
            else:
                i += (rounds - i) // (i - j) * (i - j)
            continue
        for _ in range(4):
            for y in range(len(dish)):
                for x in range(len(dish[y])):
                    if dish[y][x] is None:
                        continue
                    if dish[y][x]:
                        dish[y][x] = None
                        y_ = y
                        while y_ > 0 and dish[y_ - 1][x] is None:
                            y_ -= 1
                        dish[y_][x] = True
            dish = list(map(lambda x: list(x), zip(*dish[::-1])))
        cache[hashable] = i, tuple(map(tuple, dish))
        i += 1

    res = 0

    for y in range(len(dish)):
        for x in range(len(dish[y])):
            if dish[y][x]:
                res += len(dish) - y

    # print('\n'.join(''.join('.' if x is None else 'O' if x else '#' for x in l) for l in dish))
    print(res)