print(sum(
    int(line.split(':')[0].split(' ')[1])
    for line in open('input.txt', 'r', encoding='utf-8')
    if all(
            all(int(n) <= {'red': 12,'green': 13,'blue': 14}[col] for n, col in hand)
            for hand in [
                [g.split(' ') for g in h.split(', ')]
                for h in line.split(':')[1].strip().split('; ')
            ]
    )
))

