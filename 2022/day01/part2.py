with open('input.txt') as f:
    cur_sum = 0
    top = [0] * 3

    for line in f.readlines() + ['\n']:
        if line.strip() == '':
            top += [cur_sum]
            top.remove(min(top))
            cur_sum = 0
        else:
            cur_sum += int(line.strip())
    print(sum(top))
