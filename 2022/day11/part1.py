with open('input.txt') as f:
    monkeys = []
    monkey = None
    for line in f.readlines() + ['']:
        match line.strip().split(' '):
            case ['Monkey', _]:
                monkey = {'inspections': 0}
            case ['Starting', 'items:', *items]:
                monkey['items'] = [int(i.replace(',', '')) for i in items]
            case ['Operation:', *ops]:
                monkey['operation'] = ' '.join(ops).split(' = ')[1]
            case ['Test:', 'divisible', 'by', n]:
                monkey['test'] = {'divisible': int(n)}
            case ['If', x, 'throw', 'to', 'monkey', n]:
                monkey['test'][x[:-1]] = int(n)
            case _:
                # test = monkey['test']
                # monkey['test'] = lambda item: \
                #     test['true'] if (item % test['divisible'] == 0) else test['false']

                monkeys.append(monkey)
                monkey = None

    for r in range(20):
        for i in range(len(monkeys)):
            while monkeys[i]['items']:
                monkeys[i]['inspections'] += 1
                old = monkeys[i]['items'].pop(0)
                item = eval(monkeys[i]['operation'])
                item //= 3

                if item % monkeys[i]['test']['divisible'] == 0:
                    monkeys[monkeys[i]['test']['true']]['items'].append(item)
                else:
                    monkeys[monkeys[i]['test']['false']]['items'].append(item)
                # monkeys[monkeys[i]['test'](item)]['items'].append(item)
    m = sorted([m['inspections'] for m in monkeys])[-2:]
    print(m[0] * m[1])
