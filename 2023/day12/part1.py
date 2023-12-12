def gen_input(cogs):
    if len(cogs) == 0:
        yield []
    elif cogs[0] is None:
        for x in [True, False]:
            for y in gen_input(cogs[1:]):
                yield [x] + y
    else:
        for y in gen_input(cogs[1:]):
            yield [cogs[0]] + y

def validate(cogs, nums):
    c = 0
    n = 0
    in_group = False
    for cog in cogs:
        if cog is None:
            return False
        if cog:
            c += 1
            in_group = True
        else:
            if in_group:
                if n >= len(nums) or c != nums[n]:
                    return False
                n += 1
                c = 0
                in_group = False
    if in_group:
        if n >= len(nums) or c != nums[n]:
            return False
        n += 1
        in_group = False
    return len(nums) == n

with open('input.txt', 'r', encoding='utf-8') as f:
    data = []
    for l in f:
        cs, ns = l.strip().split()
        cs = [c == '#' if c in '#.' else None for c in cs]
        ns = list(map(int, ns.split(',')))
        data.append((cs, ns))
    print(sum(len([i for i in gen_input(cs) if validate(i, ns)]) for cs, ns in data))