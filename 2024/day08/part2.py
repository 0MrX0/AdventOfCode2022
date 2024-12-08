with open('input.txt', 'r', encoding='utf-8') as f:
    antennas: dict[str, set[tuple[int, int]]] = {}

    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c != '.':
                antennas.setdefault(c, set()).add((x, y))

    w, h = x, y

    antinodes = set()
    for freq in antennas:
        for (xa, ya), (xb, yb) in ((a, b) for a in antennas[freq] for b in antennas[freq] if a != b):
            dx, dy = xb - xa, yb - ya

            while 0 <= xa <= w and 0 <= ya <= h:
                antinodes.add((xa, ya))
                xa -= dx
                ya -= dy
            while 0 <= xb <= w and 0 <= yb <= h:
                antinodes.add((xb, yb))
                xb += dx
                yb += dy

    print(len(antinodes))
