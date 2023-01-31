from hashlib import md5


def get_input():
    text_file = open("input", "r").read()

    return text_file


def main():
    string = get_input()

    result_1, result_2 = part_one(string)
    print(f'Part One: {result_1}')
    print(f'Part Two: {result_2}')


def part_one(string):
    ans_one = 0
    ans_two = 0

    my_hash = ''

    while my_hash[0:6] != '000000':
        if not ans_one and my_hash[0:5] == '00000':
            ans_one = ans_two

        my_hash = str(md5((string + str(ans_two)).encode()).hexdigest())
        ans_two += 1

    return ans_one - 1, ans_two - 1


if __name__ == "__main__":
    main()
