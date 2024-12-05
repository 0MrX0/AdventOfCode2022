with open('input.txt', 'r', encoding='utf-8') as file:
    graph, problems = file.read().split('\n\n')

    edges = set(tuple(line.split('|')) for line in graph.split('\n'))

    out = 0
    for problem in problems.split('\n'):
        nodes = problem.split(',')
        if nodes[-1] == '':
            continue

        is_sorted = True
        for i in range(0, len(nodes) - 1):
            j = i + 1
            while j < len(nodes) and \
                    (nodes[i], nodes[j]) not in edges and \
                    (nodes[j], nodes[i]) not in edges:
                j += 1

            if j >= len(nodes) or (nodes[j], nodes[i]) in edges:
                is_sorted = False
                break

        if is_sorted:
            out += int(nodes[len(nodes) // 2])

    print(out)
