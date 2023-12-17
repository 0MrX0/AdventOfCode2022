with open('test.txt') as f:
    room = f.read().splitlines()

    energized = set()
    new_energized = set()

    beams = [((0, 5), (1, 0))] # beam: ((x, y), dx, dy))

    while len(energized) == 0 or len(new_energized - energized) > 0:
        energized |= new_energized
        new_energized = set()

        for i, ((x, y), (dx, dy)) in enumerate(beams.copy()):
            print(i, ((x, y), (dx, dy)), room[y][x])
            match room[y][x], dx, dy:
                case ('.', _, _) | ('-', _, 0) | ('|', 0, _):
                    beams[i] = ((x + dx, y + dy), (dx, dy))
                case ('/', 0, -1) | ('\\', 0, 1):
                    beams[i] = ((x + 1, y), (1, 0))
                case ('/', 0, 1) | ('\\', 0, -1):
                    beams[i] = ((x - 1, y), (-1, 0))
                case ('/', 1, 0) | ('\\', -1, 0):
                    beams[i] = ((x, y - 1), (0, -1))
                case ('/', -1, 0) | ('\\', 1, 0):
                    beams[i] = ((x, y + 1), (0, 1))
                case ('-', 0, _):
                    beams[i] = ((x + 1, y), (1, 0))
                    beams.append(((x - 1, y), (-1, 0)))
                case ('|', _, 0):
                    beams[i] = ((x, y + 1), (0, 1))
                    beams.append(((x, y - 1), (0, -1)))

        i = 0
        while i < len(beams):
            (x, y), _ = beam = beams[i]
            if beam in energized:
                beams.pop(i)
            elif 0 <= x < len(room[0]) and 0 <= y < len(room):
                new_energized.add(beam)
                i += 1
            else:
                beams.pop(i)

    energized = {(x, y) for (x, y), _ in energized}

    print(len(energized))
    # for y in range(len(room)):
    #     for x in range(len(room[0])):
    #         print(room[y][x], end='')
    #     print('\t', end='')
    #     for x in range(len(room[0])):
    #         if (x, y) in energized:
    #             print('\u2588', end='')
    #         else:
    #             print(room[y][x], end='')
    #     print()

