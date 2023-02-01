def get_input():
    text_file = open("input", "r").read().split("\n")

    full_list = []
    for line in text_file:
        line_list = [int(num) for num in line]
        full_list.append(line_list)

    return full_list


def check_north(x, y, code_input):
    list = []
    curr = code_input[y][x]

    for y_coord in range(y - 1, -1, -1):

        list.append(code_input[y_coord][x] < curr)
        if code_input[y_coord][x] >= curr:
            break
    return list


def check_south(x, y, code_input):
    list = []
    curr = code_input[y][x]

    for y_coord in range(y + 1, len(code_input)):

        list.append(code_input[y_coord][x] < curr)
        if code_input[y_coord][x] >= curr:
            break

    return list


def check_east(x, y, code_input):
    list = []
    curr = code_input[y][x]

    for x_coord in range(x + 1, len(code_input)):

        list.append(code_input[y][x_coord] < curr)
        if code_input[y][x_coord] >= curr:
            break

    return list


def check_west(x, y, code_input):
    list = []
    curr = code_input[y][x]

    for x_coord in range(x - 1, -1, -1):

        list.append(code_input[y][x_coord] < curr)
        if code_input[y][x_coord] >= curr:
            break

    return list


def main():
    code_input = get_input()

    output = part_one(code_input)
    print("Part 1:", output)

    output = part_two(code_input)
    print("Part 2:", output)


def part_one(code_input):

    visible = 0

    for y in range(0, len(code_input[0])):
        for x in range(0, len(code_input[0])):
            north = check_north(x, y, code_input)
            south = check_south(x, y, code_input)
            east = check_east(x, y, code_input)
            west = check_west(x, y, code_input)

            if all(north) or all(south) or all(east) or all(west):
                visible += 1

    return visible


def part_two(code_input):
    max = 0
    number = 0

    for y in range(0, len(code_input[0])):
        for x in range(0, len(code_input[0])):
            north = check_north(x, y, code_input)
            west = check_west(x, y, code_input)
            south = check_south(x, y, code_input)
            east = check_east(x, y, code_input)

            tree_vis = [len(north), len(west), len(south), len(east)]
            number += 1

            vision = tree_vis[0] * tree_vis[1] * tree_vis[2] * tree_vis[3]
            if vision > max:
                max = vision

    return max


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()
