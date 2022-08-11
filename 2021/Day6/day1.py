def get_input():
    with open("input.txt") as file_input:
        line_input = file_input.read().split(",")

    return line_input


def check_segments(line_segments, planes):
    pass


def main():
    fish = get_input()
    for ind in fish:
        print(ind)


if __name__ == "__main__":
    main()
