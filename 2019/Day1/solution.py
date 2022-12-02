def get_input():
    text_file = open("input", "r").read().split("\n")
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
        line = int(line)

        total += line // 3 - 2

    return total


def part_two(text_file):
    total = 0

    for line in text_file:
        num = int(line)

        while True:
            num = num // 3 - 2

            if num <= 0:
                break

            total += num

    return total


if __name__ == "__main__":
    main()
