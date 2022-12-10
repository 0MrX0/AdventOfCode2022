with open('input.txt') as f:
    x = 1
    crt = [['.' for i in range(40)] for j in range(6)]
    cycle = 0
    for line in f:
        cycle += 1
        y_, x_ = cycle // 40, cycle % 40
        if x_ in range(x, x + 3):
            crt[y_][x_ - 1] = '#'
        match line.strip().split(' '):
            case ['addx', v]:
                cycle += 1
                y_, x_ = cycle // 40, cycle % 40
                if x_ in range(x, x + 3):
                    crt[y_][x_ - 1] = '#'
                x += int(v)
    print('\n'.join([''.join(row) for row in crt]))
