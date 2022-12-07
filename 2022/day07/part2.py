import math

file_sys = {
    '/': {}
}


def go_to_path(pth: list[str]) -> dict[str, dict | str | int] | str:
    current = file_sys
    for p in pth:
        current = current[p]
    return current


def get_sizes(pth: list[str], threshold: int | None = None) -> dict[str, int]:
    if threshold is None:
        threshold = math.inf
    current = go_to_path(pth)
    p = ''.join(pth)

    sizes = {
        p: 0
    }

    for k, v in current.items():
        if isinstance(v, dict):
            c_pth = pth + [k]
            s = get_sizes(c_pth, threshold=threshold)
            sizes |= s
            sizes[p] += s[''.join(c_pth)]
        else:
            sizes[p] += v

    if sizes[p] > threshold:
        sizes[p] = math.inf
    return sizes


with open('input.txt') as f:
    path = ['/']
    for line in f:
        if line[0] == '$':
            cmd = line[1:].strip().split(' ')
            if cmd[0] == 'cd':
                directory = cmd[1]
                if directory == '/':
                    path = ['/']
                elif directory == '..':
                    path.pop()
                else:
                    path.append(directory + '/')
        else:
            ls_out = line.strip().split(' ')
            if ls_out[0] == 'dir':
                go_to_path(path)[ls_out[1] + '/'] = {}
            else:
                go_to_path(path)[ls_out[1]] = int(ls_out[0])

    free_min = 30000000 - 70000000 + get_sizes(['/'])['/']
    print(min([x for x in get_sizes(['/']).values() if x >= free_min]))
