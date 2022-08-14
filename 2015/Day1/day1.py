def get_input():
    text_file = open("input.txt", "r").read()
    return text_file


def main():
    text_file = get_input()
    get_count = check_increase(text_file)

    print(get_count)


def check_increase(text_file):
    number = 0
    index = 0
    for char in text_file:
        if number == -1:
            print(index)
        if char == "(":
            number += 1
        elif char == ")":
            number -= 1
        index += 1

    return number


if __name__ == "__main__":
    main()
