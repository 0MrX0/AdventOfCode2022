with open('input.txt') as f:
    duplicates = 0
    for line in f.readlines():
        a_desc, b_desc = line.split(',')
        a_min, a_max = map(int, a_desc.split('-'))
        b_min, b_max = map(int, b_desc.split('-'))
        a = set(range(a_min, a_max + 1))
        b = set(range(b_min, b_max + 1))
        if not (a - b) or not (b - a):
            duplicates += 1
    print(duplicates)
