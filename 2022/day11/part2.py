import math

with open('input.txt') as f:
    monkeys = []
    monkey = None
    divisibles = []
    for line in f.readlines() + ['']:
        match line.strip().split(' '):
            case ['Monkey', _]:
                monkey = {'inspections': 0}
            case ['Starting', 'items:', *items]:
                monkey['items'] = [int(i.replace(',', '')) for i in items]
            case ['Operation:', *ops]:
                operation = ' '.join(ops).split(' = ')[1]
                monkey['operation'] = lambda old, operation=operation: eval(operation)
            case ['Test:', 'divisible', 'by', n]:
                monkey['test'] = {'divisible': int(n)}
            case ['If', x, 'throw', 'to', 'monkey', n]:
                monkey['test'][x[:-1]] = int(n)
            case _:
                test = monkey['test']
                divisibles.append(test['divisible'])
                monkey['test'] = lambda item, test=test: \
                    test['true'] if (item % test['divisible'] == 0) else test['false']

                monkeys.append(monkey)
                monkey = None

    lcm = math.lcm(*divisibles)

    for r in range(10000):
        for i in range(len(monkeys)):
            while monkeys[i]['items']:
                monkeys[i]['inspections'] += 1
                item = monkeys[i]['items'].pop(0)
                item = monkeys[i]['operation'](item)
                item %= lcm

                monkeys[monkeys[i]['test'](item)]['items'].append(item)
    m = sorted([m['inspections'] for m in monkeys])[-2:]
    print(m[0] * m[1])
