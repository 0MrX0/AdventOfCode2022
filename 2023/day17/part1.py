with open('input.txt', 'r', encoding='utf-8') as f:
    nodes = [[int(x) for x in l] for l in f.read().splitlines()]

    start = (0, 0)
    end = (len(nodes[0]) - 1, len(nodes) - 1)


    def get_neighbours(node, direction = (False, False)):
        x, y = node
        dx, dy = direction

        neighbours = []

        if not dx:
            for i in range(-3, 4):
                if not i or x + i < 0 or x + i >= len(nodes[0]):
                    continue
                if i < 0:
                    cost = sum(nodes[y][x + i:x])
                else:
                    cost = sum(nodes[y][x + 1:x + i + 1])

                neighbours.append(((x + i, y), cost))
        if not dy:
            for i in range(-3, 4):
                if not i or y + i < 0 or y + i >= len(nodes):
                    continue
                if i < 0:
                    cost = sum(n[x] for n in nodes[y + i:y])
                else:
                    cost = sum(n[x] for n in nodes[y + 1:y + i + 1])
                neighbours.append(((x, y + i), cost))
        # print(('✥' if dx and dy else '↔' if dx else '↕' if dy else '⊙'), node, neighbours)
        return neighbours


    def dijkstra(start, end):
        visited = set()
        costs = {(start, (0, 0)): 0}
        queue = [(start, (0, 0))]
        while queue:
            node, d = n = queue.pop(0)
            if node == end:
                return costs[n]
            for neighbour, cost in get_neighbours(node, d):
                m = (neighbour, (bool(neighbour[0] - node[0]), bool(neighbour[1] - node[1])))
                if m in visited:
                    continue
                if m not in costs or costs[m] > costs[n] + cost:
                    costs[m] = costs[n] + cost
                    queue.append(m)
            visited.add(n)
            queue.sort(key=lambda x: costs[x])


    print(dijkstra(start, end))



    