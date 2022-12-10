with open('input.txt') as f:
    x_history = []
    x = 1
    for line in f:
        x_history.append(x)
        match line.strip().split(' '):
            case ['addx', v]:
                x_history.append(x)
                x += int(v)
    print(sum([a * b for a, b in zip(x_history[20 - 1::40], range(20, len(x_history), 40))]))
