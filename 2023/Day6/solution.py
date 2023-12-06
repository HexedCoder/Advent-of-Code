def get_input():
    with open("input") as file_input:
        puzzle_input = file_input.read().split("\n")
    lines_input = [[int(puzzle_input[0][puzzle_input[0].index(" "):].replace(" ", "")), int(puzzle_input[1][puzzle_input[1].index(" "):].replace(" ", ""))]]

    for line in puzzle_input:
        if line:
            lines_input.append(list(map(int, line.split()[1:])))
    return lines_input


def check_wins(time, record):
    start = 0
    end = 0
    for held in range(time):
        if (time - held) * held > record:
            start = held
            break

    for held in range(time, 0, -1):
        if (time - held) * held > record:
            end = held
            break

    return end - start + 1


def part_one(file_input):
    total_score = 1
    for idx, time in enumerate(file_input[0]):
        record = file_input[1][idx]
        total_score *= check_wins(time, record)

    return total_score


def part_two(file_input):
    time, record = file_input

    return check_wins(time, record)


def main():
    puzzle_input = get_input()

    part_1 = part_one(puzzle_input[1:])
    part_2 = part_two(puzzle_input[0])

    print(f"Part One:", part_1)
    print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()
