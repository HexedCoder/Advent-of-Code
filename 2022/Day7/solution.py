from collections import defaultdict
import re


def get_input():
    text_file = open("input", "r").read().split("\n")

    return text_file


def main():
    input = get_input()

    output_1, output_2 = part_one(input)
    print("Part 1:", output_1)
    print("Part 2:", output_2)


def part_one(input):
    dir_dict = defaultdict(int)
    dirs = []

    for line in input:
        line = line.split()
        if line[1] == 'cd':
            if line[2] == '..':
                dirs.pop()
            else:
                dirs.append(str(line[2]))
        if line[0].isdigit():
            for num in range(len(dirs) + 1):
                dir_dict["/".join(dirs[:num])] += int(line[0])

    totals = []

    for key in dir_dict.values():
        totals.append(key)
    print(len(dirs))
    total = 0
    for num in totals:
        if num <= 100000:
            total += num

    needed = 30000000 - (70000000 - totals[0])

    totals.sort()
    for dir in totals:
        if dir >= needed:
            needed = dir
            break

    return total, needed


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc

        print_exc()
