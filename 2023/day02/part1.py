maximum = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('input.txt', 'r', encoding='utf-8') as file:
    result = 0

    for line in file:
        x, y = map(str.strip, line.split(':'))
        game = int(x.split(' ')[1])
        hands = y.split('; ')

        possible = True
        for hand in [[g.split(' ') for g in h.split(', ')] for h in hands]:
            for n, col in hand:
                n = int(n)
                if n > maximum[col]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            result += game
    print(result)

