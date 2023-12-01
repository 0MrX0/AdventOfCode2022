with open('input.txt', 'r', encoding='utf-8') as f:
    n = 0
    for line in f:
        digits = list(filter(lambda x: x.isdigit(), line))
        n += int(digits[0] + digits[-1])
    print(n)