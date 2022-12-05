with open('input.txt') as f:
    stacks = []

    lines = f.readlines()
    i = 0
    while not lines[i][1].isdigit():
        level = lines[i][1:-1:4]
        for j in range(len(level)):
            if len(stacks) <= j:
                stacks.append([])
            if level[j] != ' ':
                stacks[j] = [level[j]] + stacks[j]
        i += 1

    for i in range(i + 2, len(lines)):
        command = list(map(int, lines[i].strip().split(' ')[1::2]))
        for j in range(command[0]):

            container = stacks[command[1] - 1].pop()
            stacks[command[2] - 1].append(container)

    code = ''
    for stack in stacks:
        code += stack[-1]
    print(code)

