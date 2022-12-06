with open('input.txt') as f:
    charsum = 0

    n = 14
    for line in f:
        for i in range(len(line)):
            if len(set(line[i:i+n])) == n:
                charsum += i + n
                break
    print(charsum)
