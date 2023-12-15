def ascii_hash(string):
    current_value = 0
    for c in string:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


with open('input.txt', 'r', encoding='utf-8') as f:
    instructions = f.read().replace('\n', '').split(',')
    print(sum(map(ascii_hash, instructions)))
