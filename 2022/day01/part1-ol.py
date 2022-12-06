print(max([sum(map(int, elf.split('\n'))) for elf in ''.join(open('input.txt').readlines()).split('\n\n')[:-1]]))
