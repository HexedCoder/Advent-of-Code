import string


def get_input():
    with open('input') as f:
        file_input = [piece for piece in [line[:-1] for line in f.read().split('\n') if line]]

    new_vals = []
    for line in file_input:
        final_idx = line.rfind('-')
        name = line[:final_idx].replace('-', ' ')
        sector_id, checksum = line[final_idx + 1:].split('[')
        new_vals.append([name, int(sector_id), checksum])

    return new_vals


def main():
    file_input = get_input()
    output, valid_lines = part_one(file_input)
    print("Part 1:", output)

    output = part_two(valid_lines)
    print("Part 2:", output)


def part_one(text_file):
    my_sum = 0
    valid_lines = []

    for name, sector_id, checksum in text_file:

        diff = ''
        for char in name:
            if char not in checksum and char != ' ':
                diff += char
        diff_count = [name.count(char) for char in diff]
        if diff_count:
            diff = max(diff_count)
        char_count = [name.count(char) for char in checksum]
        sorted_count = sorted(char_count, reverse=True)

        if char_count == sorted_count and all(char_count):
            if diff and diff > sorted_count[-1]:
                continue
            valid_lines.append([name, sector_id])
            my_sum += sector_id

    return my_sum, valid_lines


def part_two(text_file):
    letters = [char for char in string.ascii_lowercase]

    for name, sector_id in text_file:
        tmp = ''
        for char in name:
            if char in letters:
                shift = (letters.index(char) + sector_id) % 26
                tmp += letters[shift]
            else:
                tmp += char
        if 'north' in tmp:
            return sector_id


if __name__ == "__main__":
    main()
