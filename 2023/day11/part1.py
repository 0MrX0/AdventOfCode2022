with open('input.txt') as f:
    image = [[c == '#' for c in l.strip()] for l in f if l]
    expanded_columns = [not any(row[i] for row in image) for i in range(len(image[0]))]
    expanded_rows = [not any(row) for row in image]
    expanded_image = []
    for y, row in enumerate(image):
        for _ in range(1 + expanded_rows[y]):
            expanded_image.append([])
            for x, c in enumerate(row):
                for _ in range(1 + expanded_columns[x]):
                    expanded_image[-1].append(c)
    galaxies = [(x, y) for y, row in enumerate(expanded_image) for x in range(len(row)) if expanded_image[y][x]]

    print(sum(abs(x2 - x1) + abs(y2 - y1)
              for i1, (x1, y1) in enumerate(galaxies)
              for i2, (x2, y2) in enumerate(galaxies)
              if i1 < i2))