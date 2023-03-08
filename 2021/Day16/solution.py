def get_input():
    file_input = open("input").read()

    string = ''
    for letter in file_input:
        letter = (int(letter, 16))
        string = f'{string}{letter:04b}'

    return string


def main():
    string = get_input()

    output = part_one(string, 0)[1]
    print("Part 1:", output)

    output = part_two(string, 0)[1]
    print("Part 2:", output)


def part_one(string, idx):
    version = int(string[idx: idx + 3], 2)
    p_type = string[idx + 3: idx + 6]
    idx += 6

    if '100' == p_type:
        while True:
            idx += 5
            if string[idx - 5] == '0':
                break

    else:
        if '0' == string[idx]:
            packet_end = idx + 16 + int(string[idx + 1: idx + 16], 2)
            idx += 16
            while idx < packet_end:
                idx, ret = part_one(string, idx)
                version += ret

        else:
            size = int(string[idx + 1: idx + 12], 2)
            idx += 12
            for _ in range(size):
                idx, ret = part_one(string, idx)
                version += ret

    return idx, version


def part_two(string, idx):
    type = int(string[idx + 3: idx + 6], 2)
    idx += 6

    if 4 == type:
        num = 0

        while True:
            num = 16 * num + int(string[idx + 1:idx + 5], 2)
            idx += 5
            if string[idx - 5] == '0':
                break
        values = num

    else:
        values = []

        if '0' == string[idx]:
            packet_end = idx + 16 + int(string[idx + 1: idx + 16], 2)
            idx += 16
            while idx < packet_end:
                idx, ret = part_two(string, idx)
                values.append(ret)

        else:

            size = int(string[idx + 1: idx + 12], 2)
            idx += 12
            for _ in range(size):
                idx, ret = part_two(string, idx)
                values.append(ret)

    if type == 0:
        packet_value = sum(values)
    elif type == 1:
        packet_value = 1
        for num in values:
            packet_value *= num
    elif type == 2:
        packet_value = min(values)
    elif type == 3:
        packet_value = max(values)
    elif type == 4:
        packet_value = values
    elif type == 5:
        packet_value = values[0] > values[1]
    elif type == 6:
        packet_value = values[0] < values[1]
    else:
        packet_value = values[0] == values[1]

    return idx, packet_value


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc

        print_exc()
