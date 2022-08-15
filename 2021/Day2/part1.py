def get_input():
    with open("input.txt", "r") as file_input:
        lines = file_input.readlines()

    return lines


def main():
    text_file = get_input()
    increase_count = check_increase(text_file)

    print(increase_count)


def check_increase(lines):
    fwd = "forward"
    up = "up"
    down = "down"
    hor_pos = 0
    depth = 0

    for line in lines:
        line = line.split()
        if line[0] == fwd:
            hor_pos += int(line[1])
        if line[0] == up:
            depth -= int(line[1])
        if line[0] == down:
            depth += int(line[1])

    return depth * hor_pos


if __name__ == "__main__":
    main()