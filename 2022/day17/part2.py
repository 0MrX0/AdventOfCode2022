def draw(stack: list[list[bool]], rock: list[list[bool]], rx: int, ry: int) -> str:
    out = '+' + '-' * len(stack[0]) + '+\n\n'
    for y in range(1, max(len(stack), ry + len(rock))):
        tmp = '|'
        for x in range(7):
            if y - ry in range(0, len(rock)) and x - rx in range(0, len(rock[0])) and rock[y - ry][x - rx]:
                tmp += '@'
            elif y in range(0, len(stack)) and x in range(0, len(stack[0])) and stack[y][x]:
                tmp += '#'
            else:
                tmp += '.'
        out = tmp + '|\n' + out
    return out

tmp = [
    '####',
    '.#.'       '\n'
    '###'       '\n'
    '.#.',
    '..#'       '\n'
    '..#'       '\n'
    '###',
    '#'         '\n'
    '#'         '\n'
    '#'         '\n'
    '#',
    '##'        '\n'
    '##'
]

shapes = []
stack = [[True] * 7]

for x in tmp:
    shape = [[c == '#' for c in l] for l in x.split('\n')][::-1]
    shapes.append(shape)

with open('input.txt') as f:
    data = [d == '>' for d in f.read().strip() if d in '<>']

    d = 0
    for i in range(2022):
        rock = shapes[i % len(shapes)]
        rx, ry = 2, len(stack) + 3 #rock x, y
        w, h = len(rock[0]), len(rock)

        falling = True
        while falling:
            # Handle jet pushing
            if data[d]:
                if rx < 7 - w:
                    move = True
                    for y in range(h):
                        for x in range(w):
                            if ry + y < len(stack) and rock[y][x] and stack[ry + y][rx + x + 1]:
                                move = False
                    if move:
                        rx += 1
            else:
                if rx > 0:
                    move = True
                    for y in range(h):
                        for x in range(w):
                            if ry + y < len(stack) and rock[y][x] and stack[ry + y][rx + x - 1]:
                                move = False
                    if move:
                        rx -= 1
            d = (d + 1) % len(data)

            # Handle rock falling
            if ry > len(stack):
                ry -= 1
            else:
                for y in range(h):
                    for x in range(w):
                        if ry + y - 1 < len(stack) and rock[y][x] and stack[ry + y - 1][rx + x]:
                            falling = False
                            break
                ry -= 1
        for y in range(h):
            for x in range(w):
                if rock[y][x]:
                    if ry + y + 1 >= len(stack):
                        stack.append([False] * 7)
                    stack[ry + y + 1][rx + x] = True

    print(draw(stack, [[False] * 7], rx, ry))
    print(len(stack) - 1)