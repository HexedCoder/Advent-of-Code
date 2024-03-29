def get_input():
    text_file = open('puzzle_input').read()

    return text_file


def main():
    input = get_input()

    output = part_one(input)
    print("Part 1:", output)

    output = part_two(input)
    print("Part 2:", output)


def part_one(puzzle_input):
    length = len(puzzle_input)

    for num in range(0, length - 4):
        chars = set(puzzle_input[num:num + 4])

        if len(chars) == 4:
            return num + 4


def part_two(puzzle_input):
    length = len(puzzle_input)

    for num in range(0, length - 14):
        chars = set(puzzle_input[num:num + 14])

        if len(chars) == 14:
            return num + 14


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc

        print_exc()
