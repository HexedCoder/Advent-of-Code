from hashlib import md5


def get_input():
    with open('input') as f:
        file_input = f.read()

    return file_input


def main():
    file_input = get_input()
    result = part_one(file_input)
    print("Part 1:", result)

    result = part_two(file_input)
    print("Part 2:", result)


def part_one(text_file):
    code = ''
    curr_hash = ''
    num = 0

    while curr_hash[:5] != '00000':
        string = text_file + str(num)
        curr_hash = str(md5((string + str(num)).encode()).hexdigest())
        num += 1

    print(num, curr_hash)

    return code


def part_two(text_file):
    return 0


if __name__ == "__main__":
    main()
