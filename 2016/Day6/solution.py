from collections import Counter


def get_input():
    with open('input') as f:
        file_input = f.read().split('\n')

    return file_input


def main():
    file_input = get_input()
    result = part_one(file_input)
    print("Part 1:", result)

    result = part_two(file_input)
    print("Part 2:", result)


def part_one(text_file):
    valid_packets = 0

    for line in text_file:
        valid_line = False
        packet_len = len(line)
        open_bracket = 0

        for idx in range(packet_len):

            if line[idx] == '[':
                open_bracket += 1
            elif line[idx] == ']':
                open_bracket -= 1

            if idx < packet_len - 3:
                if line[idx] == line[idx + 3] and line[idx + 1] == line[idx + 2] and line[idx] != line[idx + 1]:
                    if open_bracket == 0:
                        valid_line = True
                    else:
                        valid_line = False
                        break

        if valid_line:
            valid_packets += 1

    return valid_packets


def part_two(text_file):
    valid_packets = 0

    for line in text_file:
        valid_init = False
        found = ''
        packet_len = len(line)
        open_bracket = 0

        for idx in range(packet_len):

            if line[idx] == '[':
                open_bracket += 1
            elif line[idx] == ']':
                open_bracket -= 1

            if idx < packet_len - 2:
                if line[idx] == line[idx + 2] and line[idx] != line[idx + 1]:

                    if open_bracket == 0:
                        found = line[idx:idx + 3]
                        rev = found[1] + found[0] + found[1]

                        for idx in range(packet_len):

                            if line[idx] == '[':
                                open_bracket += 1
                            elif line[idx] == ']':
                                open_bracket -= 1
                            elif idx < packet_len - 2:
                                if line[idx: idx + 3] == rev:
                                    if open_bracket != 0:
                                        valid_init = True
                                        break

        if valid_init and '[' not in found:
            valid_packets += 1

    return valid_packets


if __name__ == "__main__":
    main()
