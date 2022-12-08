def get_view_dist(x: int, y: int, dir: str, trees: list[list[int]]) -> int:
    match dir:
        case 'N':
            rng = reversed(range(0, y))
        case 'S':
            rng = range(y + 1, len(trees))
        case 'E':
            rng = range(x + 1, len(trees[0]))
        case 'W':
            rng = reversed(range(0, x))
        case _:
            raise ValueError(f'Invalid direction: {dir}')
    dist = 0
    for i in rng:
        dist += 1
        match dir:
            case 'N' | 'S':
                if trees[i][x] >= trees[y][x]:
                    return dist
            case 'E' | 'W':
                if trees[y][i] >= trees[y][x]:
                    return dist
    return dist


with open('input.txt') as f:
    trees = [list(map(int, list(line.strip()))) for line in f]

    w = len(trees[0])
    h = len(trees)
    counters = []

    for y in range(0, h):
        for x in range(0, w):
            counters += [
                get_view_dist(x, y, 'N', trees) *
                get_view_dist(x, y, 'S', trees) *
                get_view_dist(x, y, 'E', trees) *
                get_view_dist(x, y, 'W', trees)
            ]
    print(max(counters))

