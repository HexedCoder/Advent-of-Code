def get_input():
    text_file = open("input", "r").read().split("\n")
    return text_file


def main():
    text_file = get_input()

    part_one(text_file)
    part_two(text_file)


def part_one(text_file):

    total = 0

    for line in text_file:
        symbol = line[0]
        vector = int(line[1:])

        if "+" == symbol:
            total += vector
        elif "-" == symbol:
            total -= vector

    print("Part 1:", total)


def part_two(text_file):
    totals = []
    total = 0
    repeat = 0

    while not repeat:
        for line in text_file:
            symbol = line[0]
            vector = int(line[1:])

            if "+" == symbol:
                total += vector
            elif "-" == symbol:
                total -= vector

            if total in totals:
                repeat = total
                break
            totals.append(total)

    print("Part 2:", total)


if __name__ == "__main__":
    main()
