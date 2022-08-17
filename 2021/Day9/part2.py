def get_input():
    with open("input.txt") as file_input:
        lines_input = file_input.readlines()

    list_int_input = []

    for line in lines_input:

        line = line.replace("\n", "")
        line_int = []

        for num in line:
            num = int(num)
            line_int.append(num)
        list_int_input.append(line_int)

    return list_int_input


def find_lows(height_list):
    lows = []
    y = 0
    for each_line in height_list:
        x = 0
        for number in each_line:
            if x == 0:
                if y == 0:
                    if height_list[y][x + 1] > number and height_list[y + 1][
                        x] > number:
                        lows.append((x, y))

                elif y < len(height_list) - 1:

                    if height_list[y][x + 1] > number and height_list[y - 1][
                        x] > number and height_list[y + 1][x] > number:
                        lows.append((x, y))
                else:

                    if height_list[y][x + 1] > number and height_list[y - 1][
                        x] > number:
                        lows.append((x, y))
            elif x < len(each_line) - 1:

                if y == 0:
                    if height_list[y][x - 1] > number and height_list[y][
                        x + 1] > number and height_list[y + 1][x] > number:
                        lows.append((x, y))

                elif y < len(height_list) - 1:
                    if height_list[y][x - 1] > number and height_list[y][
                        x + 1] > number and height_list[y - 1][x] > number and \
                            height_list[y + 1][x] > number:
                        lows.append((x, y))

                elif y == len(height_list) - 1:
                    if height_list[y][x - 1] > number and height_list[y][
                        x + 1] > number and height_list[y - 1][x] > number:
                        lows.append((x, y))

            else:
                if y == 0:
                    if height_list[y][x - 1] > number and height_list[y + 1][
                        x] > number:
                        lows.append((x, y))

                elif y < len(height_list) - 1:
                    if height_list[y][x - 1] > number and height_list[y - 1][
                        x] > number and height_list[y + 1][x] > number:
                        lows.append((x, y))

                elif y == len(height_list) - 1:
                    if height_list[y][x - 1] > number and height_list[y - 1][
                        x] > number:
                        lows.append((x, y))

            x += 1
        y += 1

    return lows


def basin_size(height_list, map):
    width = 0
    for line in map:
        width = len(line)
    basin_sizes = []
    for basin in height_list:
        x = basin[0]
        y = basin[1]
        size = 0

        if x == len(height_list):
            break
        print(basin)

        while y > 0:
            print("a")
            print(height_list[y][x])

            if height_list[y][x] != 9:
                size += 1
                y -= 1
            else:
                break
        print("Final size", size)

        x = basin[0]
        y = basin[1]
        while y < len(map) - 1:
            print("b")

            print(height_list[y][x])

            if height_list[y][x] != 9:
                size += 1
                y += 1
            else:
                break
        print("Final size", size)

        x = basin[0]
        y = basin[1]
        while x < width - 1:
            print("c")
            print(height_list[y][x])

            if height_list[y][x] != 9:
                size += 1
                x += 1
            else:
                break
        print("Final size", size)

        x = basin[0]
        y = basin[1]
        while x > 0:
            print("d")
            x -= 1
            print(height_list[y][x])

            if height_list[y][x] != 9:
                size += 1
            else:
                break
        print("Final size", size)

        basin_sizes.append(size)
        size += 1

    basin_sizes.sort(reverse=True)

    return basin_sizes[:4]


def main():
    height_map = get_input()
    basin_points = find_lows(height_map)
    top_basin_sizes = basin_size(basin_points, height_map)

    product = 0
    index = 0
    for basin in top_basin_sizes:
        if index == 0:
            product += basin
            index += 1
        product *= basin

    print("Basin Size:", )


if __name__ == "__main__":
    main()
