from typing import Callable, Optional

with open('input.txt') as f:
    word_search = f.read().splitlines()

    hits = 0


    def check_word(word: str, x: int, y: int, direction: Optional[Callable[[int, int], tuple[int, int]]] = None) -> int:
        if word == '':
            return 1
        if not (0 <= x < len(word_search[0]) and 0 <= y < len(word_search)):
            return 0

        if direction is None:
            return sum(
                check_word(word, x, y, lambda x, y: (x + dx, y + dy))
                for dx in range (-1, 2)
                for dy in range(-1, 2)
            )

        if word_search[y][x] != word[0]:
            return 0
        new_x, new_y = direction(x, y)
        return check_word(word[1:], new_x, new_y, direction)


    for y, row in enumerate(word_search):
        for x in range(len(row)):
            hits += check_word('XMAS', x, y)

    print(hits)
