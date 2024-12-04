with open('input.txt') as f:
    word_search = f.read().splitlines()

    hits = 0


    def check_letter(
            x: int, y: int
    ) -> str | None:
        if not (0 <= x < len(word_search[0]) and 0 <= y < len(word_search)):
            return None

        return word_search[y][x]


    for y, row in enumerate(word_search):
        for x in range(len(row)):
            if check_letter(x, y) == 'A' and sum(
                    check_letter(x + i, y + j) == 'M'
                    for i in (-1, 1)
                    for j in (-1, 1)
            ) == sum(
                check_letter(x + i, y + j) == 'S'
                for i in (-1, 1)
                for j in (-1, 1)
            ) == 2 and check_letter(x - 1, y - 1) != check_letter(x + 1, y + 1):
                hits += 1

    print(hits)
