def get_input():
    text_file = open("file_input", "r").read().split("\n")

    return text_file


def main():
    file_input = get_input()

    result = part_one(file_input)
    print(f'Part One: {result}')

    result = part_two(file_input)
    print(f'Part Two: {result}')


def part_one(file_input):
    bad_strings = ['ab', 'cd', 'pq', 'xy']
    vowel = 'aeiou'

    nice_lines = 0

    for line in file_input:
        vowel_count = 0
        duplicate = False
        bad_string = False
        prev = ''

        for pair in bad_strings:
            if pair in line:
                bad_string = True
                break

        for char in line:
            curr = char
            if char in vowel:
                vowel_count += 1
            if curr == prev:
                duplicate = True
            prev = curr

        if vowel_count > 2 and duplicate and not bad_string:
            nice_lines += 1

    return nice_lines


def part_two(file_input):
    nice_lines = 0

    for line in file_input:
        duplicate = False
        repeat = False

        for num in range(len(line)):
            curr = line[num:num+2]
            if curr in line[num+2:]:
                duplicate = True

            try:
                if line[num] == line[num+2]:
                    repeat = True

            except Exception:
                pass

        if duplicate and repeat:
            nice_lines += 1

    return nice_lines


if __name__ == "__main__":
    main()
