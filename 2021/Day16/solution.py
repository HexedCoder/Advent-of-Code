def get_input():
    file_input = open("input").read()

    string = ''
    for letter in file_input:
        letter = (int(letter, 16))
        string = f'{string}{letter:04b}'

    print(string)
    return string


def main():
    string = get_input()

    output = part_one(string)
    print("Part 1:", output)


def get_literal(string, sub_length):
    num = ''
    version = string[:3]
    type_id = string[3:6]
    string = string[6:]
    read = 6

    print(version, type_id, sep='', end='')

    for start in range(1, len(string[::5]) + 1):
        sub_type = string[0]
        print(sub_type, string[1:5], sep='', end='')

        if read + start < sub_length:
            num += string[1:5]
            read += 5
            string = string[5:]
            if '0' == sub_type:
                break
            # else:
            #     print()
                # print(string)

        else:
            print(string[:sub_length - read - start], end='')
    print(' ', end='')
    print(f'{num = }')

    return read, string, int(num, 2)


def get_operator(string):
    num = ''
    version = string[:3]
    type_id = string[3:6]
    string = string[6:]

    for start in range(1, len(string[::5]) + 1):
        sub_type = string[0]

        num += string[1:5]
        string = string[5:]
        if '0' == sub_type:
            break

    print(f'{num = }')

    return string, int(num, 2)


def get_length(string, len_id):
    length = 0
    if len_id == '0':
        length = string[:15]
        print(length, end='')
    elif len_id == '1':
        length = string[:11]
        print(length, end='')
    return int(length, 2), string[11:] if '1' == len_id else string[15:]


def process_packet(string):
    version = string[:3]
    type_id = string[3:6]
    len_id = string[6]
    # print(string)
    # print(version, type_id, len_id, sep='', end='')

    return version, type_id, len_id, string[7:]


def part_one(string):

    sum = 0
    version, type_id, len_id, string = process_packet(string)

    sub_length = 0

    read = 0

    if '100' != type_id:
        sub_length, string = get_length(string, len_id)

        if '0' == len_id:
            while read < sub_length:
                ret, string, sub_val = get_literal(string, sub_length)
                print(sub_val)
                read += ret
                sum += sub_val
        else:
            while read < sub_length:
                string, sub_val = get_operator(string)
                print(sub_val)


                sum += sub_val
                read += 1

    else:
        if '0' == len_id:
            while read < sub_length:
                ret, string, sub_val = get_literal(string, sub_length)
                print(sub_val)

                read += ret
                sum += sub_val
        else:
            print('d')
            while read < sub_length:
                string, sub_val = get_operator(string)
                print(sub_val)

                sum += sub_val
                read += 1

    return sum


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc

        print_exc()
