def get_input():
    text_file = open("input", "r").read().split("\n")
    return text_file


def main():
    text_file = get_input()

    score_1 = part_one(text_file)
    print("Part 1:", score_1)

    score_2 = part_two(text_file)
    print("Part 2:", score_2)


def part_one(text_file):
    contained = 0
    assignment = []

    for line in text_file:
        line = line.split(",")
        for pair in line:
            assignment.append(pair.split("-"))

        elf_min_1 = int(assignment[0][0])
        elf_max_1 = int(assignment[0][1])
        elf_min_2 = int(assignment[1][0])
        elf_max_2 = int(assignment[1][1])

        if elf_min_1 <= elf_min_2 and elf_max_1 >= elf_max_2:
            contained += 1
        elif elf_min_2 <= elf_min_1 and elf_max_2 >= elf_max_1:
            contained += 1
        assignment = []

    return contained


def part_two(text_file):
    overlap = 0
    idx = 0
    set_1 = set()
    set_2 = set()

    for line in text_file:
        line = line.split(",")
        for pair in line:
            if 0 == idx:
                set_1 = set()
                split_1 = pair.split("-")
                split_1[0] = int(split_1[0])
                split_1[1] = int(split_1[1])
                for num in range(split_1[0], split_1[1] + 1):
                    set_1.add(num)
                idx += 1
            elif 1 == idx:

                set_2 = set()
                split_1 = pair.split("-")
                split_1[0] = int(split_1[0])
                split_1[1] = int(split_1[1])
                for num in range(split_1[0], split_1[1] + 1):
                    set_2.add(num)

                set_1 = set_1.intersection(set_2)
                if set_1:
                    overlap += 1
                idx = 0


    return overlap


if __name__ == "__main__":
    main()
