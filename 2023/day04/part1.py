with open('input.txt', 'r', encoding='utf-8') as file:
    result = 0
    for line in file:
        winning, having = map(lambda x: {int(y) for y in x.split(' ') if y}, line.split(': ')[1].split('|'))
        if len(winning & having):
            result += 2 ** (len(winning & having) - 1)
    print(result)
