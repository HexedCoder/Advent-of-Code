def convert_words(input_file):
    conversions = {"one": "1e", "two": "2o", "three": "3e", "four": "4r", "five": "5e", "six": "6x", "seven": "7n", "eight": "8t", "nine": "9e"}

    while True:
        min_idx = 99
        rep_word = ""
        for word, num in conversions.items():
            idx = input_file.find(word)
            if -1 < idx < min_idx:
                min_idx = idx
                rep_word = word
        if min_idx != 99:
            input_file = input_file.replace(rep_word, conversions[rep_word])
        else:
            break

    return input_file


def get_input():
    with open("input") as file_input:
        puzzle_input = file_input.read().split("\n")
        lines_input = []

        for line in puzzle_input:
            lines_input.append(line)

    return lines_input


def part_one(file_input):
    total = 0

    for line in file_input:
        if line:
            line = [char for char in line if char.isdigit()]
            if line:
                total += int(line[0] + line[-1])

    return total


def part_two(file_input):
    total = 0

    for line in file_input:
        if line:
            line = convert_words(line)
            line = [char for char in line if char.isdigit()]
            print(line, int(line[0] + line[-1]))
            total += int(line[0] + line[-1])

    return total


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
