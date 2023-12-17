with open('input.txt', 'r', encoding='utf-8') as f:
    nodes = [[int(x) for x in l] for l in f.read().splitlines()]

    start = (0, 0)
    end = (len(nodes[0]) - 1, len(nodes) - 1)


    def get_neighbours(node, direction = (False, False)):
        x, y = node
        dx, dy = direction

        neighbours = []

        if not dx:
            for i in range(4, 11):
                if 0 <= x - i < len(nodes[0]):
                    neighbours.append(((x - i, y), sum(nodes[y][x - i:x])))
                if 0 <= x + i < len(nodes[0]):
                    neighbours.append(((x + i, y), sum(nodes[y][x + 1:x + i + 1])))
        if not dy:
            for i in range(4, 11):
                if 0 <= y - i < len(nodes):
                    neighbours.append(((x, y - i), sum(n[x] for n in nodes[y - i:y])))
                if 0 <= y + i < len(nodes):
                    neighbours.append(((x, y + i), sum(n[x] for n in nodes[y + 1:y + i + 1])))
        return neighbours


    def dijkstra(start, end):
        visited = set()
        costs = {(start, (False, False)): 0}
        queue = [(start, (False, False))]
        prevs = {(start, (False, False)): None}
        while queue:
            node, d = n = queue.pop(0)
            if node == end:
                return costs[n]
            for neighbour, cost in get_neighbours(node, d):
                m = (neighbour, (bool(neighbour[0] - node[0]), bool(neighbour[1] - node[1])))
                if m in visited:
                    continue
                prevs[m] = n
                if m not in costs or costs[m] > costs[n] + cost:
                    costs[m] = costs[n] + cost
                    queue.append(m)
            visited.add(n)
            queue.sort(key=lambda x: costs[x])

    print(dijkstra(start, end))



    