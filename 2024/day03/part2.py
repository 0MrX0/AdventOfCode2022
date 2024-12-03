import re

with open('input.txt', 'r', encoding='utf-8') as f:
    regex = re.compile(r'do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)')

    s = 0

    enabled = True
    for line in f:
        for m in regex.finditer(line):
            match m.group(0).split('(')[0]:
                case 'do':
                    enabled = True
                case 'don\'t':
                    enabled = False
                case 'mul':
                    if enabled:
                        a = int(m.group(1))
                        b = int(m.group(2))
                        s += a * b
    print(s)
