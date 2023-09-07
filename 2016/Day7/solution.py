from collections import Counter


def get_input():
    with open('input') as f:
        file_input = f.read().split('\n')

    return file_input


def main():
    file_input = get_input()
    result1, result2 = part_one(file_input)
    print("Part 1:", result1)
    print("Part 2:", result2)


def part_one(text_file):
    line_size = len(text_file[0])
    letter_list = ['' for _ in range(line_size)]

    for line in text_file:
        for idx, letter in enumerate(line):
            letter_list[idx] += letter

    return ''.join([Counter(line).most_common(1)[0][0] for line in letter_list]), ''.join([Counter(line).most_common()[-1][0] for line in letter_list])


if __name__ == "__main__":
    main()
