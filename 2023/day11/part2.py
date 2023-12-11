with open('input.txt') as f:
    image = [[c == '#' for c in l.strip()] for l in f if l]
    expanded_columns = [not any(row[i] for row in image) for i in range(len(image[0]))]
    expanded_rows = [not any(row) for row in image]

    expanded = 1000000

    galaxies = []
    for y, row in enumerate(image):
        y_offset = (expanded - 1) * sum(expanded_rows[:y])
        for x, c in enumerate(row):
            x_offset = (expanded - 1) * sum(expanded_columns[:x])
            if c:
                galaxies.append((x + x_offset, y + y_offset))

    print(sum(abs(x2 - x1) + abs(y2 - y1)
              for i1, (x1, y1) in enumerate(galaxies)
              for i2, (x2, y2) in enumerate(galaxies)
              if i1 < i2))