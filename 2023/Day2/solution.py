def get_input():
    with open("input") as file_input:
        puzzle_input = file_input.read().split("\n")
        lines_input = []

        for line in puzzle_input:
            lines_input.append(line)

    return lines_input


def part_one(file_input):
    for line in file_input:
        print(line)

    return 0


def part_two(file_input):
    return "In Progress"


def main():
    puzzle_input = get_input()

    part_1 = part_one(puzzle_input)
    part_2 = part_two(puzzle_input)

    print(f"Part One:", part_1)
    print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()
