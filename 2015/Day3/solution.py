def get_input():
    text_file = open("input", "r").read()

    return text_file[:-1]

def main():
    string = get_input()

    result = part_one(string)
    print(f'Part One: {result}')

    result = part_two(string)
    print(f'Part Two: {result}')


def part_one(string):
    houses = [(0,0)]
    x = 0
    y = 0

    for char in string:
        if '^' == char:
            y += 1
        elif 'v' == char:
            y -= 1
        elif '>' == char:
            x += 1
        else:
            x -= 1
        houses.append((x,y))

    return len(set(houses))


def part_two(string):
    houses = [(0,0)]
    x_1 = 0
    y_1 = 0

    x_2 = 0
    y_2 = 0

    for idx, char in enumerate(string):
        mod = idx % 2
        if '^' == char:
            if not mod:
                y_1 += 1
            else:
                y_2 += 1
        elif 'v' == char:
            if not mod:
                y_1 -= 1
            else:
                y_2 -= 1
        elif '>' == char:
            if not mod:
                x_1 += 1
            else:
                x_2 += 1
        else:
            if not mod:
                x_1 -= 1
            else:
                x_2 -= 1

        houses.append((x_1,y_1) if not mod else (x_2,y_2))

    return len(set(houses))


if __name__ == "__main__":
    main()
