with open('input.txt') as f:
    prio = 0
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        tmp = [l.strip() for l in lines[i:i+3]]

        for c in tmp[0]:
            if c in tmp[1] and c in tmp[2]:
                if c.islower():
                    prio += ord(c) - ord('a') + 1
                else:
                    prio += ord(c) - ord('A') + 27
                break
    print(prio)

