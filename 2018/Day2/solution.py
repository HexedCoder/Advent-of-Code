def get_input():
    with open('input') as f:
        file_input = f.read().split('\n')

    return file_input


def char_count(line):
    two = False
    three = False

    for char in line:
        if line.count(char) == 2:
            two = True
        elif line.count(char) == 3:
            three = True

    return two, three


def part_one(inputs):
    valid_2 = 0
    valid_3 = 0

    for line in inputs:
        two, three = char_count(line)
        valid_2 += two
        valid_3 += three

    return valid_2 * valid_3


def check_diff(curr, line):
    diff = 0
    string = ''

    for idx, char in enumerate(curr):
        if char != line[idx]:
            diff += 1
        else:
            string += char

    if diff != 1:
        return None

    return string


def part_two(inputs):
    for curr in inputs:
        for line in inputs:
            diff = check_diff(curr, line)

            if diff:
                return diff


def main():
    inputs = get_input()

    print('Part One:', part_one(inputs))
    print('Part Two:', part_two(inputs))


if __name__ == "__main__":
    main()
