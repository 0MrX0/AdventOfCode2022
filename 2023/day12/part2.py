cache = {}

def gen_input(cogs, nums, in_group=False):
    global cache
    key = (tuple(cogs), tuple(nums), in_group)
    if key in cache:
        return cache[key]
    res = 0
    if len(cogs) == 0:
        if len(nums) == 0 or (len(nums) == 1 and nums[0] == 0):
            res += 1
    elif cogs[0] is None:
        if len(nums) == 0:
            nums = [0]
        n, *ns = nums
        if n > 0:
            res += gen_input(cogs[1:], [(n - 1)] + ns, True)
            if not in_group:
                res +=  gen_input(cogs[1:], [n] + ns)
        else:
            res += gen_input(cogs[1:], ns)
    else:
        if len(nums) == 0:
            nums = [0]
        n, *ns = nums
        if n > 0:
            if cogs[0]:
                res += gen_input(cogs[1:], [(n - 1)] + ns, True)
            if not cogs[0] and not in_group:
                res += gen_input(cogs[1:], [n] + ns)
        elif not cogs[0]:
            res += gen_input(cogs[1:], ns)

    cache[key] = res
    return res

with open('input.txt', 'r', encoding='utf-8') as f:
    data = []
    for l in f:
        cs, ns = l.strip().split()
        cs = [c == '#' if c in '#.' else None for c in cs]
        cs = ((cs + [None]) * 5)[:-1]
        ns = list(map(int, ns.split(','))) * 5
        data.append((cs, ns))
    print(sum(gen_input(cs, ns) for cs, ns in data))