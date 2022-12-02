def get_input():
    text_file = open("input.txt", "r").read()
    return text_file


def main():
    text_file = get_input()
    outcome, first = track_santa(text_file)

    print("Part 1:", outcome)
    print("Part 2:", first)


def track_santa(text_file):
    number = 0
    index = 1
    first = [0, 0]

    for char in text_file:
        if char == "(":
            number += 1
        elif char == ")":
            number -= 1

        if number < 0 and not first[0]:
            first[0] = 1
            first[1] = index

        index += 1

    return number, first[1]


if __name__ == "__main__":
    main()
