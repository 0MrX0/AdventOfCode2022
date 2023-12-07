ranks = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

hand_is = {
    'five of a kind': lambda h: len(set(h)) == 1,
    'four of a kind': lambda h: any(h.count(r) == 4 for r in ranks),
    'full house': lambda h: any(h.count(r) == 3 for r in ranks) and len(set(h)) == 2,
    'three of a kind': lambda h: any(h.count(r) == 3 for r in ranks),
    'two pairs': lambda h: sum(h.count(r) == 2 for r in ranks) == 2,
    'one pair': lambda h: any(h.count(r) == 2 for r in ranks),
    'high card': lambda h: len(set(h)) == 5
}
types = list(hand_is.keys())

with open('input.txt', 'r', encoding='utf-8') as file:
    hands = [(line.split(' ')[0], int(line.split(' ')[1])) for line in file]

    hands_sorted = sorted(
        hands,
        key=lambda h: (
            types.index([x for x in hand_is if hand_is[x](h[0])][0]),
            *(ranks.index(x) for x in h[0] if x in ranks)
        ),
        reverse=True
    )

    result = 0

    for i, (hand, bid) in enumerate(hands_sorted):
        result += bid * (i + 1)

    print(result)
