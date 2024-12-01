with open('input.txt', 'r', encoding='utf-8') as f:
    list_a, list_b = map(
        sorted,
        zip(*(
            tuple(map(int, line.split()))
            for line in f
        ))
    )
    print(sum(
        x * list_b.count(x) for x in list_a
    ))
