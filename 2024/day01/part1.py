with open('input.txt', 'r', encoding='utf-8') as f:
    print(
        sum(
            abs(b - a)
            for a, b in zip(
                *map(
                    sorted, zip(*(
                        tuple(map(int, line.split()))
                        for line in f
                    ))
                )
            )
        )
    )
