import json

def compare(left: int | list[int | list[any]], right: int | list[int | list[any]]) -> tuple[bool, bool]:
    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, int):
        return left <= right, left < right
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            if i < len(right):
                c = compare(left[i], right[i])
                if not c[0]:
                    return False, False
                if c[1]:
                    return True, True
            else:
                return False, False
        return True, len(left) < len(right)
    return False, False

with open('input.txt') as f:
    pairs = [tuple(json.loads(x) for x in p.split('\n')) for p in (f.read() + '\n').split('\n\n')[:-1]]

    print(sum(p + 1 for p in range(len(pairs)) if compare(*pairs[p])[1]))
