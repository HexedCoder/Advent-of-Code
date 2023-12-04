def get_input():
    with open("input") as file_input:
        puzzle_input = file_input.read().split("\n")
        lines_input = []

        for line in puzzle_input:
            if line:
                lines_input.append(line.split(":")[1])

    return lines_input


def part_one(file_input):
    total = 0

    for line in file_input:
        win, curr = [set(num.split()) for num in line.split('|')]
        total += 1 << len(win.intersection(curr)) - 1 if len(win.intersection(curr)) else 0

    return total


def part_two(file_input):
    total_cards = [1 for _ in file_input]

    for idx, line in enumerate(file_input):
        win, curr = [set(num.split()) for num in line.split('|')]

        for num in range(len(win.intersection(curr))):
            total_cards[idx + num + 1] += total_cards[idx]

    return sum(total_cards)


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
