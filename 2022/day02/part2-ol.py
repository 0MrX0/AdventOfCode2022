print(sum([({0: 3, 1: 1, 2: 2} if b == 'X' else {0: 4, 1: 5, 2: 6} if b == 'Y' else {0: 8, 1: 9, 2: 7})[ord(a) - ord('A')] for a, b in [line.strip().split(' ') for line in open('input.txt')]]))
