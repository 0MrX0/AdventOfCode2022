import re

with open('input.txt', 'r', encoding='utf-8') as f:
    regex = re.compile(r'mul\((\d+),(\d+)\)')

    s = 0

    for line in f:
        for m in regex.finditer(line):
            a = int(m.group(1))
            b = int(m.group(2))
            s += a * b

    print(s)
