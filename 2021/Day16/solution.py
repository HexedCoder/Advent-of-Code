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
    type = string[idx + 3: idx + 6]
    idx += 6

    if '100' == type:
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
        version = sum(values)
    elif type == 1:
        version = 1
        for num in values:
            version *= num
    elif type == 2:
        version = min(values)
    elif type == 3:
        version = max(values)
    elif type == 4:
        version = values
    elif type == 5:
        version = values[0] > values[1]
    elif type == 6:
        version = values[0] < values[1]
    else:
        version = values[0] == values[1]

    return idx, version


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc

        print_exc()
