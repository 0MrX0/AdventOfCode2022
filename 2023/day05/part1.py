from collections import namedtuple

Range = namedtuple('Range', ['min', 'max'])

keys = ['seed']

with open('input.txt', 'r', encoding='utf-8') as f:
    se, *ms = ''.join(f.readlines()).split('\n\n')
    seeds = {int(seed): int(seed) for seed in se.split(':')[1].split(' ') if seed}

    maps = {}
    for m in ms:
        if not m:
            continue
        a2b, *ranges = m.split('\n')
        a, b = a2b.split(' ')[0].split('-to-')
        maps[(a, b)] = []
        keys +=[b]

        for r in ranges:
            if not r:
                continue
            dest_a, source_a, length = map(int, r.split(' '))

            maps[(a, b)] += [(Range(source_a, source_a + length), dest_a - source_a)]
        maps[(a, b)] = sorted(maps[(a, b)], key=lambda x: x[0].min)

    for i in range(1, len(keys)):
        cur_map = maps[(keys[i - 1], keys[i])]
        for seed, value in seeds.items():
            for r, o in cur_map:
                if r.min <= value < r.max:
                    seeds[seed] += o
                    break

    print(min(seeds.values()))