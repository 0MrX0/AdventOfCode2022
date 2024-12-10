with open('input.txt', 'r', encoding='utf-8') as f:
    topography = [[int(c) for c in line.strip()] for line in f]

    starting_points: list[tuple[int, int]] = [
        (x, y)
        for y in range(len(topography))
        for x in range(len(topography[y]))
        if topography[y][x] == 0
    ]

    ending_points: list[tuple[int, int]] = []


    def follow_path(point: tuple[int, int], prev_height: int) -> None:
        x, y = point

        if x < 0 or x >= len(topography[0]) or y < 0 or y >= len(topography):
            return

        height = topography[y][x]
        if height != prev_height + 1:
            return

        if height == 9:
            ending_points.append(point)
            return

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_point = (x + dx, y + dy)
            follow_path(new_point, height)


    for point in starting_points:
        follow_path(point, -1)

    print(len(ending_points))
