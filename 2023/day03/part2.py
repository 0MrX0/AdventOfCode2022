from itertools import product

with open('input.txt', 'r', encoding='utf-8') as f:
    schematic = [l.strip() + '.' for l in f]
    schematic.append('.' * len(schematic[0]))

    gears = {}

    for y, line in enumerate(schematic):
        number = ''
        for x, c in enumerate(line):
            if c.isdigit():
                number += c
            elif number:
                l = len(number)
                adj_gears = [(i, j)
                             for i, j in product(range(x - l - 1, x + 1), range(y - 1, y + 2))
                             if schematic[j][i] == '*']
                for gear in adj_gears:
                    if gear not in gears:
                        gears[gear] = []
                    gears[gear] += [int(number)]
                number = ''
    print(sum(
        gear[0] * gear[1]
        for gear in gears.values()
        if len(gear) == 2
    ))