with open('input.txt', 'r', encoding='utf-8') as file:
    cards = [tuple(map(lambda x: {int(y) for y in x.split(' ') if y}, line.split(': ')[1].split('|'))) for line in file]
    num_of_cards = {idx: 1 for idx in range(len(cards))}

    for idx, (winning, having) in enumerate(cards):
        for i in range(len(winning & having)):
            num_of_cards[idx + i + 1] += num_of_cards[idx]

    print(sum(num_of_cards.values()))
