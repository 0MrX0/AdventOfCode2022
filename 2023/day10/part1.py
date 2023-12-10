with open('input.txt') as f:
    graph = {}
    start = (-1, -1)
    for y, line in enumerate(f.read().split('\n')):
        for x, c in enumerate(line):
            graph[(x, y)] = {
                'n': (x, y - 1) if c in set('|LJ') else None,
                's': (x, y + 1) if c in set('|F7') else None,
                'e': (x + 1, y) if c in set('-FL') else None,
                'w': (x - 1, y) if c in set('-J7') else None
            }
            if c == 'S':
                start = (x, y)
    drones = [
        ((start[0], start[1] - 1), 's', 1),
        ((start[0], start[1] + 1), 'n', 1),
        ((start[0] + 1, start[1]), 'w', 1),
        ((start[0] - 1, start[1]), 'e', 1)
    ]
    for drone in drones: # cleanup drones
        if drone[0] not in graph:
            drones.remove(drone)
            continue
        if graph[drone[0]][drone[1]] is None:
            drones.remove(drone)
            continue
    scanning = True
    while scanning:
        for i, drone in enumerate(drones):
            if any(drone[0] == d[0] for d in drones if d != drone):
                scanning = False
                print(drone[2])
                break
            pipe = graph[drone[0]]
            for d in set('nsew') - set(drone[1]):
                if pipe[d] is not None:
                    d_ = 'n' if d == 's' else 's' if d == 'n' else 'e' if d == 'w' else 'w'
                    drones[i] = (pipe[d], d_, drone[2] + 1)
                    break
