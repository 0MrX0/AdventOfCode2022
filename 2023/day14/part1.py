with open('input.txt', 'r', encoding='utf-8') as f:
    dish = [[None if x == '.' else x == 'O' for x in l.strip()] for l in f if l.strip()]

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

    # print('\n'.join(''.join(' ' if x is None else 'O' if x else '#' for x in l) for l in dish))

    res = 0

    for y in range(len(dish)):
        for x in range(len(dish[y])):
            if dish[y][x]:
                res += len(dish) - y

    print(res)