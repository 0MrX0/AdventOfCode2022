from itertools import cycle

with open('input.txt') as f:
    dirs, _, *ns = f.read().splitlines()

    directions = cycle((int(d == 'R')) for d in dirs)
    nodes = {n[:3]: (n[7:10], n[12:15]) for n in ns}

    node = 'AAA'
    i = 0
    while node != 'ZZZ':
        node = nodes[node][next(directions)]
        i += 1
    print(i)

