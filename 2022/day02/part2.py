def get_score(i_str: str, strat: str) -> int:
    i = ord(i_str) - ord('A')
    match strat:
        case 'X':
            return {0: 2, 1: 0, 2: 1}[i] + 1
        case 'Y':
            return i + 4
        case 'Z':
            return {0: 1, 1: 2, 2: 0}[i] + 7
        case _:
            raise ValueError(f'Invalid strategy: {strat}')


with open('input.txt') as f:
    score = 0
    for line in f:
        a, b = line.strip().split(' ')
        score += get_score(a, b)

    print(score)
