with open('input.txt') as f:
    cur_sum = 0
    top3 = [0, 0, 0]

    for line in f.readlines() + ['\n']:
        if line[:-1] == '':
            top3 += [cur_sum]
            top3.remove(min(top3))
            cur_sum = 0
        else:
            cur_sum += int(line[:-1])
    print(cur_sum, top3)
    print(sum(top3))
