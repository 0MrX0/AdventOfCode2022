def reverse_d(d):
    return 'n' if d == 's' else 's' if d == 'n' else 'e' if d == 'w' else 'w'


def get_offset(d):
    return (0, -1) if d == 'n' else (0, 1) if d == 's' else (1, 0) if d == 'e' else (-1, 0)


with open('input.txt') as f:
    lines = f.read().split('\n')

    max_x = len(lines[0])
    max_y = len(lines)

    graph = {}
    start = (-1, -1)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            graph[(x, y)] = {
                'n': (x, y - 1) if c in set('|LJ') else None,
                's': (x, y + 1) if c in set('|F7') else None,
                'e': (x + 1, y) if c in set('-FL') else None,
                'w': (x - 1, y) if c in set('-J7') else None
            }
            if c == 'S':
                start = (x, y)

    ds = [
        ((start[0] + get_offset(d)[0], start[1] + get_offset(d)[1]), reverse_d(d), 1) for d in 'nsew'
    ]
    drones = []

    pipes = set()
    pipes.add(start)

    for drone in ds:  # cleanup drones
        if drone[0] in graph and graph[drone[0]][drone[1]] is not None:
            drones.append(drone)

    graph[start] = {
        reverse_d(d): (x, y) for ((x, y), d, _) in drones
    }

    drone = drones[0]
    while drone[0] not in pipes:
        pipes.add(drone[0])
        pipe = graph[drone[0]]
        for d in set('nsew') - set(drone[1]):
            if pipe[d] is not None:
                d_ = reverse_d(d)
                drone = (pipe[d], d_, drone[2] + 1)
                break

    for node in graph:
        if node in pipes:
            graph[node] = {k: v for k, v in graph[node].items() if v is not None}
        else:
            graph[node] = {}


    def expand(graph):
        graph_ = {}
        for node in graph:
            x, y = node
            node_ = (2 * x, 2 * y)
            graph_[node_] = {}
            for d in graph[node]:
                d_ = reverse_d(d)
                new_node = (2 * x + get_offset(d)[0], 2 * y + get_offset(d)[1])
                graph_[node_][d] = new_node

                if new_node not in graph_:
                    graph_[new_node] = {}
                graph_[new_node][d_] = node_

        # add a border of empty nodes
        for y in range(-1, 2 * max(y for (_, y) in graph) + 2):
            for x in range(-1, 2 * max(x for (x, _) in graph) + 2):
                if (x, y) not in graph_:
                    graph_[(x, y)] = {}
        return graph_


    def bfs(start, graph):
        visited = set()
        queue = [start]
        while len(queue) > 0:
            node = queue.pop(0)
            x, y = node
            if node not in graph or graph[node] or node in visited:
                visited.add(node)
                continue
            visited.add(node)
            for d in 'nsew':
                x_ = x + get_offset(d)[0]
                y_ = y + get_offset(d)[1]
                queue.append((x_, y_))
        return visited


    shrunk_visited = {
        (x // 2, y // 2)
        for (x, y) in bfs((-1, -1), expand(graph))
        if x % 2 == 0 and y % 2 == 0
    }

    nodes = set(graph.keys())
    print(len(nodes - shrunk_visited - pipes))
