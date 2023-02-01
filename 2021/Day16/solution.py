def get_input():
    file_input = open("input").read()

    return file_input


def main():
    input = get_input()

    output = part_one(input)
    print("Part 1:", output)


def part_one(file_input):
    print(file_input)

    string = ''
    for letter in file_input:
        letter = (int(letter, 16))
        string = f'{string}{letter:04b}'

    version = string[:3]
    type_id = string[3:6]

    if '100' == type_id:
        for _ in range(len(string[7:])):
            print(string[_], end=' ')
        print()

    print(string, version, type_id)

    return 0


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc

        print_exc()
