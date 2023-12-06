with open('input.txt', 'r', encoding='utf-8') as f:
    a, b, *_ = f.read().split('\n')
    times = [int(x) for x in a.split(' ')[1:] if x]
    distances = [int(x) for x in b.split(' ')[1:] if x]

    result = 1

    for i in range(len(times)):
        t = times[i]
        c = 0
        for x in range(t):
            d = x * (t - x)
            if d > distances[i]:
                c += 1
        result *= c


    print(f'{result}')
