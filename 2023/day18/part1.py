with open('input.txt', 'r', encoding='utf-8') as f:
    instructions = []
    for line in f:
        if not line.strip():
            continue
        d, n, c = line.strip().split()
        instructions.append((d, int(n), c[1:-1]))

    dug_out = {}
    min_x, min_y = 0, 0
    max_x, max_y = 0, 0
    x, y = 0, 0
    for d, n, _ in instructions:
        if d in 'UD':
            dug_out[x, y] = d
        for _ in range(n):
            match d:
                case 'U':
                    y -= 1
                case 'D':
                    y += 1
                case 'R':
                    x += 1
                case 'L':
                    x -= 1
            dug_out[x, y] = d
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)


    c = 0
    for y in range(min_y - 1, max_y + 2):
        toggle = False
        pre_dir = None
        for x in range(min_x - 1, max_x + 2):
            if (x, y) in dug_out:
                if dug_out[x, y] != pre_dir and dug_out[x, y] in 'UD':
                    toggle = not toggle
                    pre_dir = dug_out[x, y]
                c += 1
            elif toggle:
                c += 1
    print(c)