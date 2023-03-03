def get_input():
    text_file = open('input').read()
    return text_file


def main():
    text_file = get_input()

    total = part_one(text_file)
    print("Part 1:", total)
    total = part_two(text_file)
    print("Part 2:", total)


def part_one(text_file):
    total = 0
    file_len = len(text_file) - 1

    for num in range(file_len):
        if 1 == len(set(text_file[num:num+2])):
            total += int(text_file[num])

    if text_file[-1] == text_file[0]:
        total += int(text_file[0])

    return total


def part_two(text_file):
    total = 0
    file_len = len(text_file)
    loop = len(text_file) // 2

    for idx in range(file_len):
        next_cmp = idx - loop
        if text_file[idx] == text_file[next_cmp]:
            total += int(text_file[idx])

    return total


if __name__ == "__main__":
    main()
