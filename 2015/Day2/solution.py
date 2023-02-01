def get_input():
    text_file = open('input').readlines()
    return text_file


def main():
    text_file = get_input()
    increase_count = part_one(text_file)
    print("Part 1:", increase_count)
    increase_count = part_two(text_file)
    print("Part 2:", increase_count)


def part_one(lines):
    totals = []
    dims = []

    for line in lines:
        line = line.split("x")
        length = int(line[0])
        width = int(line[1])
        height = int(line[2])

        dims.append(length * width)
        dims.append(width * height)
        dims.append(height * length)
        dims.sort()

        totals.append(dims[0] + (2 * sum(dims)))

        dims = []

    return sum(totals)


def part_two(lines):
    totals = []
    dims = []

    for line in lines:
        line = line.split("x")
        length = int(line[0])
        width = int(line[1])
        height = int(line[2])

        dims.append(2 * length)
        dims.append(2 * width)
        dims.append(length * width * height)

        totals.append(sum(dims))
        dims = []

    return sum(totals)


if __name__ == "__main__":
    main()