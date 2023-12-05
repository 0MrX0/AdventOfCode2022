from collections import namedtuple

Range = namedtuple('Range', ['min', 'max'])

keys = ['seed']

with open('input.txt', 'r', encoding='utf-8') as f:
    se, *ms = ''.join(f.readlines()).split('\n\n')
    nums = [int(x) for x in se.split(':')[1].split(' ') if x]
    seeds = sorted([Range(start, start + length) for start, length in zip(nums[::2], nums[1::2])], key=lambda x: x.min)

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
        j = 0
        while j < len(seeds):
            seed_min, seed_max = seeds[j]
            for r, o in cur_map:
                if r.min <= seed_min < r.max:
                    print(seed_min, seed_max, r, o, (seed_min + o, min(seed_max, r.max) + o))
                    seeds[j] = Range(seed_min + o, min(seed_max, r.max) + o)
                    if seed_max > r.max:
                        seeds.insert(j + 1, Range(r.max, seed_max))
                    break
            j += 1
        seeds = sorted(seeds, key=lambda x: x.min) # sort
        for j in range(len(seeds) - 1): # merge
            if seeds[j].max >= seeds[j + 1].min:
                seeds[j] = Range(seeds[j].min, seeds[j + 1].max)
                seeds.pop(j + 1)
                break

    print(min(seeds, key=lambda x: x.min).min)

