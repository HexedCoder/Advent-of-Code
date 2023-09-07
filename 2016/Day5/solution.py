from hashlib import md5


def get_input():
    with open('input') as f:
        file_input = f.read()

    return file_input


def main():
    file_input = get_input()
    # result = part_one(file_input)
    # print("Part 1:", result)

    result = part_two(file_input)
    print("Part 2:", result)


def part_one(text_file):
    code = ''
    num = 0

    while len(code) < 8:
        string = text_file + str(num)
        curr_hash = str(md5((string).encode()).hexdigest())
        if curr_hash[:5] == '00000':
            code += curr_hash[5]
        num += 1

    return code


def part_two(text_file):
    code = [-1, -1, -1, -1, -1, -1, -1, -1]
    num = 0

    while -1 in code:
        string = text_file + str(num)
        curr_hash = md5(string.encode()).hexdigest()
        if curr_hash[:5] == '00000' and -1 < int(curr_hash[5], 16) < 8 and code[int(curr_hash[5])] == -1:
            code[int(curr_hash[5])] = curr_hash[6]
        num += 1

    return ''.join(str(val) for val in code)


if __name__ == "__main__":
    main()
