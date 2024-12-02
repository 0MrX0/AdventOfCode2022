with open('input.txt', 'r', encoding='utf-8') as f:
    reports = tuple(map(lambda x: tuple(map(int, x.split())), f))

    safe = 0

    for report in reports:
        report_sorted = sorted(report)

        safe += (
            all(x == y for x,y in zip(report, report_sorted)) or
            all(x == y for x,y in zip(reversed(report), report_sorted))
        ) and  all(
            0 < abs(report[i - 1] - report[i]) < 4
            for i in range(1, len(report))
        )

    print(safe)