def get_input():
    text_file = open("s_input", "r").read().split("\n")
    return text_file


def main():
    text_file = get_input()

    for line in text_file:
        print(line)


if __name__ == "__main__":
    main()
