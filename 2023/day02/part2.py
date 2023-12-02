with open('input.txt', 'r', encoding='utf-8') as file:
    result = 0

    for line in file:
        x, y = map(str.strip, line.split(':'))
        game = int(x.split(' ')[1])
        hands = y.split('; ')

        minimum = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for hand in [[g.split(' ') for g in h.split(', ')] for h in hands]:
            for n, col in hand:
                n = int(n)
                if n > minimum[col]:
                    minimum[col] = n

        result += minimum['red'] * minimum['green'] * minimum['blue']
    print(result)

