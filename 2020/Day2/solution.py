def get_input():
    password_list = []

    text_file = open("input", "r").read().split("\n")

    for line in text_file:
        amount, req_letter, password = line.split()

        curr = [int(num) for num in amount.split('-')]
        curr.append(req_letter.split(':')[0])
        curr.append(password)
        password_list.append(curr)

    return password_list


def main():
    password_list = get_input()

    part_1, part_2 = get_count(password_list)
    print("Part 1:", part_1)
    print("Part 2:", part_2)


def get_count(password_list):
    valid_p1 = 0
    valid_p2 = 0
    password: str

    for min_cnt, max_cnt, char, password in password_list:
        # Part 1 Check
        count = password.count(char)
        if min_cnt <= count <= max_cnt:
            valid_p1 += 1

        # Part 2 Check
        either = char == password[min_cnt - 1] or char == password[max_cnt - 1]
        match = password[min_cnt - 1] == password[max_cnt - 1]
        if either and not match:
            valid_p2 += 1

    return valid_p1, valid_p2


if __name__ == "__main__":
    main()
