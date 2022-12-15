import re

with open('input.txt') as f:
    signals = set()
    for line in f:
        sx, sy, bx, by = map(int, [re.sub(r'[^0-9]+', '', l) for l in line.split('=')][1:])
        dist = abs(sx - bx) + abs(sy - by)
        signals.add(((sx, sy), dist))

    r = range(0, 4000000 + 1)
    c = (-1, -1)
    for y in r:
        x = 0
        while x < r.stop:
            for (sx, sy), d in signals:
                if abs(sy - y) > d:
                    continue
                dd = d - abs(y - sy)
                min_x = sx - dd
                max_x = sx + dd + 1
                if x in range(min_x, max_x):
                    x = max_x
            if (x, y) == c:
                print('found', (x, y), x * 4000000 + y)
                exit()
            c = (x, y)
        print(f'finished y={y}/{r.stop - 1}')
