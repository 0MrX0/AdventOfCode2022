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
    packets = [json.loads(p.strip()) for p in f if p.strip()] + [[[2]], [[6]]]

    for _ in range(len(packets)):
        for i in range(len(packets) - 1):
            if not compare(packets[i], packets[i + 1])[1]:
                tmp = packets[i]
                packets[i] = packets[i + 1]
                packets[i + 1] = tmp
    i2 = None
    i6 = None
    for i in range(len(packets)):
        if packets[i] == [[2]]:
            i2 = i + 1
        elif packets[i] == [[6]]:
            i6 = i + 1
    print(i2 * i6)
