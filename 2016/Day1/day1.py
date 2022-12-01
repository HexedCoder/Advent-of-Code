def get_input():
    text_file = open("input", "r").read().split()
    return text_file


def main():
    y_x = [0,0]  # NWSE
    curr_direction = 0

    text_file = get_input()
    for line in text_file:
        line = line.replace(",",  "")

        if "R" == line[0]:
            curr_direction += 1

        elif "L" == line[0]:
            curr_direction -= 1

        curr_direction %= 4

        if 0 == curr_direction:
            y_x[0] -= int(line[1:])
        elif 1 == curr_direction:
            y_x[1] += int(line[1:])
        elif 2 == curr_direction:
            y_x[0] += int(line[1:])
        elif 3 == curr_direction:
            y_x[1] -= int(line[1:])

    ans = abs(y_x[0]) + abs(y_x[1])

    print("Part 1:", ans)


if __name__ == "__main__":
    main()
