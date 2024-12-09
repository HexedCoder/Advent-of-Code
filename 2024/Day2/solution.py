def get_input():
    with open("input") as _input:
        line_input = _input.readlines()
    reports = []
    for line in line_input:
        line = list(map(int, line.split()))
        reports.append(line)
    return reports


def get_direction(report, dir):
    if dir == "asc":
        return all(0 < (report[i + 1] - report[i]) < 4 for i in range(len(report) - 1))
    else:
        return all(0 < (report[i] - report[i + 1]) < 4 for i in range(len(report) - 1))


def validate_report(report, part_two):
    if get_direction(report, "asc") or get_direction(report, "dsc"):
        return 1

    if part_two:
        for i in range(len(report)):
            temp_report = report[:i] + report[i + 1:]
            if get_direction(temp_report, "asc") or get_direction(temp_report, "dsc"):
                return 1

    return 0


def part_1(reports):
    valid_count = 0
    for report in reports:
        valid_count += validate_report(report, False)
    return valid_count


def part_2(reports):
    valid_count = 0
    for report in reports:
        valid_count += validate_report(report, True)
    return valid_count


def main():
    reports = get_input()
    print("Part 1:", part_1(reports))
    print("Part 2:", part_2(reports))


if __name__ == "__main__":
    main()
