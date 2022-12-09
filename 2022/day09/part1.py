visited = set()
head = (0, 0)
tail = (0, 0)

with open('input.txt') as f:
    for line in f:
        d, n = line.strip().split(' ')
        for i in range(int(n)):
            match d:
                case 'U':
                    head = (head[0], head[1] + 1)
                case 'D':
                    head = (head[0], head[1] - 1)
                case 'L':
                    head = (head[0] - 1, head[1])
                case 'R':
                    head = (head[0] + 1, head[1])

            if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
                if tail[0] == head[0]:
                    tail = (tail[0], tail[1] + 1 if tail[1] < head[1] else tail[1] - 1)
                elif tail[1] == head[1]:
                    tail = (tail[0] + 1 if tail[0] < head[0] else tail[0] - 1, tail[1])
                else:
                    tail = (tail[0] + 1 if tail[0] < head[0] else tail[0] - 1,
                            tail[1] + 1 if tail[1] < head[1] else tail[1] - 1)
            visited.add(tail)
    print(len(visited))
