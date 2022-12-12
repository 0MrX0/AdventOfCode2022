def get_current_height(char: str) -> int:
    match char:
        case 'S':
            return 0
        case 'E':
            return 25
        case _:
            return ord(char) - ord('a')


def dijkstra(
        x: int, y: int,
        routes: list[list[tuple[int, int]]],
        nodes: list[list[dict[str, int | tuple[int, int] | bool]]]
):
    n = (x, y)
    while n is not None:
        d = nodes[n[1]][n[0]]['dist'] + 1
        for i, j in routes[n[1]][n[0]]:
            if nodes[j][i]['dist'] > d or nodes[j][i]['dist'] == -1:
                nodes[j][i]['dist'] = d
                nodes[j][i]['prev'] = (n[1], n[0])

        nodes[n[1]][n[0]]['visited'] = True

        # find next
        n = None
        for i in range(len(nodes)):
            for j in range(len(nodes[i])):
                if nodes[i][j]['dist'] != -1 and not nodes[i][j]['visited']:
                    if n is None or nodes[i][j]['dist'] < nodes[n[1]][n[0]]['dist']:
                        n = (j, i)



with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

    nodes = []
    routes = []
    start = None
    end = None

    for y in range(len(lines)):
        routes.append([])
        nodes.append([])
        for x in range(len(lines[y])):
            if lines[y][x] == 'S':
                start = (x, y)
            elif lines[y][x] == 'E':
                end = (x, y)
            h = get_current_height(lines[y][x])
            route = []
            for i in [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]:
                if 0 <= i[0] < len(lines[y]) and 0 <= i[1] < len(lines):
                    if get_current_height(lines[i[1]][i[0]]) - h <= 1:
                        route.append(i)
            routes[y].append(route)
            nodes[y].append({'dist': -1, 'prev': None, 'visited': False})

    nodes[start[1]][start[0]]['dist'] = 0

    dijkstra(start[1], start[0], routes, nodes)

    print(nodes[end[1]][end[0]]['dist'])



