from tqdm import tqdm
cache = {}

def gen_input(cogs, nums, in_group=False):
    global cache
    key = (tuple(cogs), tuple(nums), in_group)
    if key in cache:
        return cache[key]
    res = []
    if len(cogs) == 0:
        if len(nums) == 0 or (len(nums) == 1 and nums[0] == 0):
            res.append([])
    elif cogs[0] is None:
        if len(nums) == 0:
            nums = [0]
        n, *ns = nums
        if n > 0:
            for y in gen_input(cogs[1:], [(n - 1)] + ns, True):
                res.append([True] + y)
            if not in_group:
                for y in gen_input(cogs[1:], [n] + ns):
                    res.append([False] + y)
        else:
            for y in gen_input(cogs[1:], ns):
                res.append([False] + y)
    else:
        if len(nums) == 0:
            nums = [0]
        n, *ns = nums
        if n > 0:
            if cogs[0]:
                for y in gen_input(cogs[1:], [(n - 1)] + ns, True):
                    res.append([cogs[0]] + y)
            if not cogs[0] and not in_group:
                for y in gen_input(cogs[1:], [n] + ns):
                    res.append([cogs[0]] + y)
        elif not cogs[0]:
            for y in gen_input(cogs[1:], ns):
                res.append([cogs[0]] + y)

    cache[key] = res
    return res

with open('input.txt', 'r', encoding='utf-8') as f:
    # f = ['.# 1']
    data = []
    for l in f:
        cs, ns = l.strip().split()
        cs = [c == '#' if c in '#.' else None for c in cs]
        cs = ((cs + [None]) * 5)[:-1]
        ns = list(map(int, ns.split(','))) * 5
        data.append((cs, ns))
    print(sum(len(gen_input(cs, ns)) for cs, ns in tqdm(data)))