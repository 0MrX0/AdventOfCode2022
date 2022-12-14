with open('input.txt') as f:
    rock = [list(tuple(map(int, q.strip().split(','))) for q in p.split('->')) for p in f]
    x_range = (min(min(x[0] for x in p) for p in rock), max(max(x[0] for x in p) for p in rock))
    y_range = 0, max(max(q[1] for q in p) for p in rock)

    occupied = set()
    for p in rock:
        for q in range(len(p) - 1):
            xa, ya = p[q]
            xb, yb = p[q + 1]
            while xa != xb or ya != yb:
                occupied.add((xa, ya))
                if xa < xb:
                    xa += 1
                elif xa > xb:
                    xa -= 1
                if ya < yb:
                    ya += 1
                elif ya > yb:
                    ya -= 1
        occupied.add(p[-1])


    generating = True
    i = 0
    while (500, 0) not in occupied:
        x, y = 500, 0
        stop = False
        while not stop:
            if (x, y + 1) not in occupied and y + 1 < y_range[1] + 2:
                y += 1
            elif (x - 1, y + 1) not in occupied and y + 1 < y_range[1] + 2:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in occupied and y + 1 < y_range[1] + 2:
                x += 1
                y += 1
            else:
                occupied.add((x, y))
                stop = True
                i += 1

    print(i)
