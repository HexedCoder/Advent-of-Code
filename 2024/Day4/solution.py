def get_input():
    with open("input") as _input:
        line_input = _input.readlines()

    return line_input


def horizontal_reverse_check(report):
    xmas = 0
    samx = 0
    for line in report:
        xmas += line.count("XMAS")
        samx += line.count("SAMX")

    return xmas + samx


def vertical_check(report):
    count = 0
    for i in range(len(report) - 3):
        for j in range(len(report[i])):
            if report[i][j] == "X" and report[i + 1][j] == "M" and report[i + 2][j] == "A" and report[i + 3][j] == "S":
                count += 1
            if report[i][j] == "S" and report[i + 1][j] == "A" and report[i + 2][j] == "M" and report[i + 3][j] == "X":
                count += 1
    return count

def diagnonal_check(report):
    count = 0
    for i in range(len(report)):
        for j in range(len(report[i])):
            try:
                if report[i][j] == "X" and report[i + 1][j + 1] == "M" and report[i + 2][j + 2] == "A" and report[i + 3][j + 3] == "S":
                    count += 1
            except IndexError:
                pass
            try:
                if j > 2 and report[i][j] == "X" and report[i + 1][j - 1] == "M" and report[i + 2][j - 2] == "A" and report[i + 3][j - 3] == "S":
                    count += 1
            except IndexError:
                pass
            try:
                if j > 2 and i > 2 and report[i][j] == "X" and report[i - 1][j - 1] == "M" and report[i - 2][j - 2] == "A" and report[i - 3][j - 3] == "S":
                    count += 1
            except IndexError:
                pass
            try:
                if i > 2 and report[i][j] == "X" and report[i - 1][j + 1] == "M" and report[i - 2][j + 2] == "A" and report[i - 3][j + 3] == "S":
                    count += 1
            except IndexError:
                pass
    return count

def x_check(report):
    count = 0
    for i in range(1, len(report) - 1):
        for j in range(1, len(report[i]) - 1):
            if report[i][j] == "A":
                if (report[i + 1][j + 1] == "M" and report[i - 1][j - 1] == "S") or (report[i + 1][j + 1] == "S" and report[i - 1][j - 1] == "M"):
                    if (report[i + 1][j - 1] == "M" and report[i - 1][j + 1] == "S") or (report[i + 1][j - 1] == "S" and report[i - 1][j + 1] == "M"):
                        count += 1
    return count


def part_1(reports):
    valid_count = 0
    valid_count += horizontal_reverse_check(reports)
    valid_count += vertical_check(reports)
    valid_count += diagnonal_check(reports)

    return valid_count


def part_2(reports):
    valid_count = 0
    valid_count += x_check(reports)

    return valid_count


def main():
    reports = get_input()
    print("Part 1:", part_1(reports))
    print("Part 2:", part_2(reports))


if __name__ == "__main__":
    main()
