with open('input.txt', 'r', encoding='utf-8') as f:

    def solve(equation, solution):
        if len(equation) == 1:
            return equation[0] == solution

        for operator in (lambda x, y: x + y, lambda x, y: x * y):
            new_equation = equation[1:]
            new_equation[0] = operator(equation[0], equation[1])
            if solve(new_equation, solution):
                return True
        return False


    count = 0
    for line in f:
        solution, equation = line.strip().split(': ')
        solution = int(solution)
        equation = list(map(int, equation.split(' ')))

        if solve(equation, solution):
            count += solution

    print(count)
