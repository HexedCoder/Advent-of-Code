def get_input():
    with open("input.txt", "r") as file_input:
        lines = file_input.readlines()

    return lines


def main():
    text_file = get_input()
    increase_count1 = check_increase_part_1(text_file)
    increase_count2 = check_increase_part_2(text_file)

    print("Part 1:", increase_count1)
    print()
    print("Part 2:", increase_count2)


def check_increase_part_1(lines):
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


def check_increase_part_2(lines):
    fwd = "forward"
    up = "up"
    down = "down"
    hor_pos = 0
    aim = 0
    depth = 0

    for line in lines:
        line = line.split()
        if line[0] == fwd:
            hor_pos += int(line[1])
            depth += aim * int(line[1])
        if line[0] == up:
            aim -= int(line[1])
        if line[0] == down:
            aim += int(line[1])

    return depth * hor_pos


if __name__ == "__main__":
    main()
