def ascii_hash(string):
    current_value = 0
    for c in string:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


with open('input.txt', 'r', encoding='utf-8') as f:
    instructions = f.read().replace('\n', '').split(',')

    boxes = [[] for _ in range(256)]
    for instruction in instructions:
        if instruction[-1] == '-':
            label = instruction[:-1]
            for i, lens in enumerate(boxes[ascii_hash(label)]):
                if lens[0] == label:
                    boxes[ascii_hash(label)].pop(i)
                    break
        else:
            label, focal_length = instruction.split('=')
            bs = boxes[ascii_hash(label)]
            for i, (lbl, fl) in enumerate(bs):
                if lbl == label:
                    bs[i] = (lbl, int(focal_length))
                    break
            else:
                bs.append((label, int(focal_length)))

    print(sum((i + 1) * (j + 1) * fl for i, box in enumerate(boxes) for j, (_, fl) in enumerate(box)))

