with open('input.txt', 'r', encoding='utf-8') as f:
    room = []

    pos = tuple()

    for y, line in enumerate(f):
        room.append([])
        for x, c in enumerate(line.strip()):
            room[y].append(c == '#')
            if c == '^':
                pos = (x, y, 0)

    visited = set()
    positions = set()

    while pos not in visited:
        visited.add(pos)
        positions.add(pos[:2])
        x, y, d = pos

        match d:
            case 0:
                front = (x, y - 1)
            case 1:
                front = (x + 1, y)
            case 2:
                front = (x, y + 1)
            case 3:
                front = (x - 1, y)

        if not (0 <= front[0] < len(room[0]) and 0 <= front[1] < len(room)):
            pass
        elif room[front[1]][front[0]]:
            pos = (x, y, (d + 1) % 4)
        else:
            pos = (*front, d)


    print(
        len(
            positions
        )
    )
