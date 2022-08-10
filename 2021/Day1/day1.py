def get_input():
    text_file = open("input.txt", "r").read().split("\n")
    return text_file


def main():
    text_file = get_input()
    increase_count = check_increase(text_file)

    print(increase_count)


def check_increase(text_file):
    current = 0
    line_count = 0
    increase_count = 0
    for line in text_file:
        line = int(line)
        if line_count == 0:
            current = line
            line_count += 1

        previous = current
        current = line
        if current > previous:
            increase_count += 1
    return increase_count


if __name__ == "__main__":
    main()