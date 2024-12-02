with open('input.txt', 'r', encoding='utf-8') as f:
    reports = tuple(map(lambda x: tuple(map(int, x.split())), f))

    safe = 0

    for report in reports:
        for i in range(len(report) + 1):
            report_cpy = list(report)

            if (i > 0):
                report_cpy.pop(i - 1)

            report_sorted = sorted(report_cpy)

            if (
                all(x == y for x,y in zip(report_cpy, report_sorted)) or
                all(x == y for x,y in zip(reversed(report_cpy), report_sorted))
            ) and  all(
                0 < abs(report_cpy[i - 1] - report_cpy[i]) < 4
                for i in range(1, len(report_cpy))
            ):
                safe += 1
                break

    print(safe)