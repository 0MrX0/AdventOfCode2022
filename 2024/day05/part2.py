with open('input.txt', 'r', encoding='utf-8') as file:
    graph, problems = file.read().split('\n\n')

    edges = set(tuple(line.split('|')) for line in graph.split('\n'))

    cache = {}
    def is_sorted(nodes):
        if tuple(nodes) in cache:
            return cache[tuple(nodes)]
        for i in range(0, len(nodes) - 1):
            j = i + 1
            while j < len(nodes) and \
                    (nodes[i], nodes[j]) not in edges and \
                    (nodes[j], nodes[i]) not in edges:
                j += 1

            if j >= len(nodes) or (nodes[j], nodes[i]) in edges:
                cache[tuple(nodes)] = False
                return False
        cache[tuple(nodes)] = True
        return True


    out = 0
    for problem in problems.split('\n'):
        nodes = problem.split(',')
        if nodes[-1] == '':
            continue

        if not is_sorted(nodes):
            while not is_sorted(nodes):
                for i in range(0, len(nodes) - 1):
                    for j in range(i + 1, len(nodes)):
                        if (nodes[j], nodes[i]) in edges:
                            nodes[i], nodes[j] = nodes[j], nodes[i]
            out += int(nodes[len(nodes) // 2])

    print(out)
