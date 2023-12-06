with open('input.txt', 'r', encoding='utf-8') as f:
    a, b, *_ = f.read().split('\n')
    time = int(a.split(':')[1].replace(' ', ''))
    distance = int(b.split(':')[1].replace(' ', ''))

    result = 1

    t = time
    c = 0
    for x in range(t):
        d = x * (t - x)
        if d > distance:
            c += 1
    result *= c


    print(f'{result}')
