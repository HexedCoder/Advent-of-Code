def get_input():
    text_file = open('input').read().split()
    return text_file


def main():
    y_x = [0, 0]  # NS WE
    curr_direction = 0

    text_file = get_input()
    locations = []
    repeat = []

    for line in text_file:
        line = line.replace(',', '')

        if 'R' == line[0]:
            curr_direction += 1

        elif 'L' == line[0]:
            curr_direction -= 1

        curr_direction %= 4

        for num in range(int(line[1:])):

            if 0 == curr_direction:
                y_x[0] -= 1

            elif 1 == curr_direction:
                y_x[1] += 1

            elif 2 == curr_direction:
                y_x[0] += 1

            elif 3 == curr_direction:
                y_x[1] -= 1

            if [y_x[0], y_x[1]] not in locations:
                locations.append([y_x[0], y_x[1]])
            else:
                if not repeat:
                    repeat = [y_x[0], y_x[1]]

    print('Part 1:', abs(y_x[0]) + abs(y_x[1]))
    print('Part 2:', abs(repeat[0]) + abs(repeat[1]))


if __name__ == "__main__":
    main()
