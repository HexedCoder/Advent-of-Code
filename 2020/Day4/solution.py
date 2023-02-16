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
    req_attrs_ranges = {'eyr': (2019, 2031), 'iyr': (2009, 2021),
                        'hgt': [(149, 194), (58, 77)], 'byr': (1919, 2003)}
    req_attrs_cont = {'hcl': '0123456789abcdef', 'pid': (),
                      'ecl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']}
    valid = 0
    attrs = []
    EOF = len(file_input) - 1

    for idx, line in enumerate(file_input):
        line = line.split()
        for field in line:
            if field[:3] != 'cid':
                attrs.append((field[:3], field[4:]))

        if not line or idx == EOF:
            invalid = False

            for attr, val in attrs:
                if attr in req_attrs_ranges:
                    if 'hgt' == attr:
                        type = val[-2:]
                        if type not in ['cm', 'in']:
                            invalid = True
                        else:
                            try:
                                num = int(val[:-2])
                                if 'cm' == type:
                                    if not req_attrs_ranges[attr][0][0] < num < req_attrs_ranges[attr][0][1]:
                                        invalid = True
                                elif 'in' == type:
                                    if not req_attrs_ranges[attr][1][0] < num < req_attrs_ranges[attr][1][1]:
                                        invalid = True

                            except ValueError:
                                invalid = True

                    elif not req_attrs_ranges[attr][0] < int(val) < req_attrs_ranges[attr][1]:
                        invalid = True

                elif attr in req_attrs_cont:
                    if 'hcl' == attr:
                        if '#' != val[0] or any(char not in req_attrs_cont[attr] for char in val[1:]):
                            invalid = True

                    elif 'pid' == attr:
                        if len(val) != 9 or not val.isdigit():
                            invalid = True

                    elif 'ecl' == attr:
                        if len(val) != 3 or val not in req_attrs_cont[attr]:
                            invalid = True

            if not invalid and len(attrs) == 7:
                valid += 1
            attrs = []

    return valid


if __name__ == "__main__":
    main()
