with open('input.txt') as f:
    prio = 0
    for line in f:
        tmp = line.strip()
        comp0 = tmp[:len(tmp) // 2]
        comp1 = tmp[len(tmp) // 2:]

        for c in comp0:
            if c in comp1:
                if c.islower():
                    prio += ord(c) - ord('a') + 1
                else:
                    prio += ord(c) - ord('A') + 27
                break
    print(prio)

