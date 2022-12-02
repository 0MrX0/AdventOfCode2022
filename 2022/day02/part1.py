def get_score(i_str: str, o_str: str) -> int:
    i = ord(i_str) - ord('A')
    o = ord(o_str) - ord('X')
    if i == o:  # draw
        return o + 4
    if (i, o) in ((0, 1), (1, 2), (2, 0)):  # win
        return o + 7
    return o + 1  # lose


with open('input.txt') as f:
    score = 0
    for line in f:
        a, b = line.strip().split(' ')
        score += get_score(a, b)

    print(score)
