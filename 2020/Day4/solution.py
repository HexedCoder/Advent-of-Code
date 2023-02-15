def get_input():
    file_input = open('input').readlines()

    return file_input


def main():
    file_input = get_input()

    total = part_one(file_input)
    print("Part 1:", total)

    total = part_two(file_input)
    print("Part 2:", total)


def part_one(file_input):
    req_attrs = ['hcl', 'eyr', 'pid', 'iyr', 'ecl', 'hgt', 'byr']
    valid = 0
    attrs = []
    EOF = len(file_input) - 1

    for idx, line in enumerate(file_input):
        line = line.split()
        for field in line:
            attrs.append(field[:3])

        if not line or idx == EOF:
            if sum([1 if attr in req_attrs else 0 for attr in attrs]) > 6:
                valid += 1
            attrs = []

    return valid


def part_two(file_input):
    req_attrs_ranges = {'eyr': (2020, 2031), 'iyr': (2010, 2021),
                        'hgt': [(150, 194), (59, 77)], 'byr': (1920, 2003)}
    req_attrs_cont = {'hcl': '123456789abcdef', 'pid': (),
                      'ecl': ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')}
    valid = 0
    attrs = []
    EOF = len(file_input) - 1

    for idx, line in enumerate(file_input):
        line = line.split()
        for field in line:
            attrs.append((field[:3], field[4:]))

        invalid = False
        if not line or idx == EOF:
            for attr, val in attrs:
                if attr in req_attrs_ranges:
                    if 'hgt' == attr:
                        try:
                            type = val[-2:]
                            num = int(val[:-2])
                            if 'cm' == type:
                                if not req_attrs_ranges[attr][0][0] <= int(
                                        num) < req_attrs_ranges[attr][0][1]:
                                    invalid = True
                            elif 'in' == type:
                                if not req_attrs_ranges[attr][1][0] <= int(
                                        num) < req_attrs_ranges[attr][1][1]:
                                    invalid = True
                            else:
                                invalid = True

                        except:
                            invalid = True

                    elif not req_attrs_ranges[attr][0] <= int(val) < \
                             req_attrs_ranges[attr][1]:
                        invalid = True
                elif attr in req_attrs_cont:
                    if 'hcl' == attr:
                        chars = val[1:]
                        for char in chars:
                            if char not in req_attrs_cont[attr]:
                                invalid = True
                        if '#' != val[0]:
                            invalid = True

                    elif 'pid' == attr:
                        if len(val) != 9 or int(val) < -1:
                            invalid = True

                    elif 'ecl' == attr:
                        if len(val) != 3:
                            invalid = True

                        if val not in req_attrs_cont[attr]:
                            invalid = True

            if not invalid:
                valid += 1
            attrs = []

    return valid


if __name__ == "__main__":
    main()
