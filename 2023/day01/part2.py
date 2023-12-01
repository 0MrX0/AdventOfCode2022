numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
with open('input.txt', 'r', encoding='utf-8') as f:
    n = 0
    for line in f:
        for s in numbers:
            line = line.replace(s, s + numbers[s] + s)
        digits = list(filter(lambda x: x.isdigit(), line))
        n += int(digits[0] + digits[-1])
    print(n)

