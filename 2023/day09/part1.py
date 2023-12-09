def get_next(history):
    diffs = []
    for i, j in zip(history, history[1:]):
        diffs += [j - i]
    if not any(diffs):
        return history[-1]
    return history[-1] + get_next(diffs)


with open('input.txt', 'r', encoding='utf-8') as file:
    histories = [list(map(int, l.split())) for l in file]

    result = 0

    for history in histories:
        result += get_next(history)

    print(result)
