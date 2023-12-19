with open('input.txt', 'r', encoding='utf-8') as f:
    rule_string, in_string = map(lambda x: [y for y in x.split('\n') if y], f.read().split('\n\n'))

    rules = { # exec done, accepted
        'A': lambda *_: True,
        'R': lambda *_: True,
    }
    for r in rule_string:
        name, rule = r.split('{')
        checks = rule.strip('}').split(',')
        parsed_rules = []
        for check in checks:
            if ':' in check:
                k, l = check.split(':')
                n = int(k[2:])
                match k[:2]:
                    case 'x>':
                        o = (lambda n: (lambda x, m, a, s: x > n))(n)
                    case 'x<':
                        o = (lambda n: (lambda x, m, a, s: x < n))(n)
                    case 'm>':
                        o = (lambda n: (lambda x, m, a, s: m > n))(n)
                    case 'm<':
                        o = (lambda n: (lambda x, m, a, s: m < n))(n)
                    case 'a>':
                        o = (lambda n: (lambda x, m, a, s: a > n))(n)
                    case 'a<':
                        o = (lambda n: (lambda x, m, a, s: a < n))(n)
                    case 's>':
                        o = (lambda n: (lambda x, m, a, s: s > n))(n)
                    case 's<':
                        o = (lambda n: (lambda x, m, a, s: s < n))(n)
                parsed_rules.append((o, l))
            else:
                parsed_rules.append((lambda *_: True, check))
        rules[name] = parsed_rules


    all_vars = []
    for i in in_string:
        j = i[1:-1]
        all_vars.append(tuple(int(k.split('=')[1]) for k in j.split(',')))

    c = 0

    for var in all_vars:
        r = 'in'
        while r not in ['A', 'R']:
            for rule in rules[r]:
                if rule[0](*var):
                    r = rule[1]
                    break
        if r == 'A':
            c += sum(var)
    print(c)
