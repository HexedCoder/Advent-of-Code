with open("input", 'rb') as f:
    actual = f.read().decode('utf-8')

def clean_input(line_input):
    line_input = [line[1:line.find(')')] if ',' in line[1:line.find(')')] else "" for line in line_input.split('mul') if line[0] == '(' and ')' in line]

    return line_input

def remove_dont_care(line_input):
    result = []
    skip = False
    for part in line_input.split("don't()"):
        if skip:
            if "do()" in part:
                result.append(part[part.find("do()"):])
        else:
            result.append(part)

        skip = True
    return ' '.join(result)

def part_1(line_input):
    line_input = clean_input(line_input)
    total = 0
    for line in line_input:
        try:
            x, y = line.split(',')
            total += int(x) * int(y)
        except ValueError:
            pass
    return total


def part_2(line_input):
    line_input = remove_dont_care(line_input)
    line_input = clean_input(line_input)
    total = 0
    for line in line_input:
        try:
            x, y = line.split(',')
            total += int(x) * int(y)
        except ValueError:
            pass
    return total

def main():
    print("Part 1:", part_1(actual))
    print("Part 2:", part_2(actual))


if __name__ == "__main__":
    main()
