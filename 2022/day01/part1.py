with open('input.txt') as f:
    cur_sum = 0
    max_sum = 0

    for line in f.readlines() + ['\n']:
        if line.strip() == '':
            max_sum = max(max_sum, cur_sum)
            cur_sum = 0
        else:
            cur_sum += int(line.strip())
    print(max_sum)
