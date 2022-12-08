def hidden(x: int, y: int, dir: str, trees: list[list[int]]) -> int:
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
                    return True
            case 'E' | 'W':
                if trees[y][i] >= trees[y][x]:
                    return True
    return False


with open('input.txt') as f:
    trees = [list(map(int, list(line.strip()))) for line in f]

    w = len(trees[0])
    h = len(trees)
    counter = 2 * w + 2 * h - 4

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if not(
                    hidden(x, y, 'N', trees) and
                    hidden(x, y, 'S', trees) and
                    hidden(x, y, 'E', trees) and
                    hidden(x, y, 'W', trees)):
                counter += 1
    print(counter)

