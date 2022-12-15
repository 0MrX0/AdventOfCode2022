import re

with open('input.txt') as f:
    signals = set()
    beacons = set()
    for line in f:
        sx, sy, bx, by = map(int, [re.sub(r'[^0-9]+', '', l) for l in line.split('=')][1:])
        dist = abs(sx - bx) + abs(sy - by)
        signals.add(((sx, sy), dist))
        beacons.add((bx, by))

    x_range = (min(x - d for (x, y), d in signals), max(x + d for (x, y), d in signals))
    y = 2000000
    c = sum(
        1 for x in range(x_range[0], x_range[1] + 1)
        if (x, y) not in beacons and any(abs(x - sx) + abs(y - sy) <= d for (sx, sy), d in signals)
    ) # TODO: optimize this
    print(c)
