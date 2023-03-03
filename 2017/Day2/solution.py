def get_input():
    text_file = [str(l).split('\t') for l in open('input').read().split('\n')]
    text_file = [list(map(int, line)) for line in text_file]
    return text_file


def main():
    text_file = get_input()

    total = part_one(text_file)
    print("Part 1:", total)
    total = part_two(text_file)
    print("Part 2:", total)


def part_one(text_file):
    total = 0

    for line in text_file:
        total += max(line) - min(line)
    return total


def part_two(text_file):
    total = 0

    for list_ in text_file:

        total += sum([check // num for check in list_ for num in list_ if
                      check != num and check % num == 0])

    return total


if __name__ == "__main__":
    main()
