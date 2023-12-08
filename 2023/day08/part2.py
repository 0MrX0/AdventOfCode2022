import math
from itertools import cycle

with open('input.txt') as f:
    dirs, _, *ns = f.read().splitlines()

    directions = cycle((int(d == 'R')) for d in dirs)
    nodes = {n[:3]: (n[7:10], n[12:15]) for n in ns}

    nodes_i = [(n, 0) for n in nodes if n[-1] == 'A']
    while any(n[-1] != 'Z' for n, _ in nodes_i):
        d = next(directions)
        nodes_i = [(nodes[n][d], i + 1) if n[-1] != 'Z' else (n, i) for n, i in nodes_i]

    result = math.lcm(*list(zip(*nodes_i))[1])
    print(result)
