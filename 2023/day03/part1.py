from itertools import product

with open('input.txt', 'r', encoding='utf-8') as f:
    schematic = [l.strip() + '.' for l in f]
    schematic.append('.' * len(schematic[0]))

    part_sum = 0

    for y, line in enumerate(schematic):
        number = ''
        for x, c in enumerate(line):
            if c.isdigit():
                number += c
            elif number:
                l = len(number)
                if any(schematic[j][i] != '.' and not schematic[j][i].isdigit()
                       for i, j in product(range(x - l - 1, x + 1), range(y - 1, y + 2))):
                    part_sum += int(number)
                number = ''
    print(part_sum)