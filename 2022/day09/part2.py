visited = set()
knots = [(0, 0)] * 10

with open('input.txt') as f:
    for line in f:
        d, n = line.strip().split(' ')
        for i in range(int(n)):
            match d:
                case 'U':
                    knots[0] = (knots[0][0], knots[0][1] + 1)
                case 'D':
                    knots[0] = (knots[0][0], knots[0][1] - 1)
                case 'L':
                    knots[0] = (knots[0][0] - 1, knots[0][1])
                case 'R':
                    knots[0] = (knots[0][0] + 1, knots[0][1])

            for j in range(1, len(knots)):
                if abs(knots[j][0] - knots[j - 1][0]) > 1 or abs(knots[j][1] - knots[j - 1][1]) > 1:
                    if knots[j][0] == knots[j - 1][0]:
                        knots[j] = (knots[j][0], knots[j][1] + 1 if knots[j][1] < knots[j - 1][1] else knots[j][1] - 1)
                    elif knots[j][1] == knots[j - 1][1]:
                        knots[j] = (knots[j][0] + 1 if knots[j][0] < knots[j - 1][0] else knots[j][0] - 1, knots[j][1])
                    else:
                        knots[j] = (knots[j][0] + 1 if knots[j][0] < knots[j - 1][0] else knots[j][0] - 1,
                                knots[j][1] + 1 if knots[j][1] < knots[j - 1][1] else knots[j][1] - 1)
            visited.add(knots[j])
    print(len(visited))
