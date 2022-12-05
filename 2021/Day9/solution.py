width = 0
bottom = 0
_map = []


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
    basin_coord = []
    basin_nums = []
    y = 0
    for each_line in height_list:
        x = 0
        for number in each_line:
            if x == 0:
                if y == 0:
                    if height_list[y][x + 1] > number and \
                            height_list[y + 1][x] > number:
                        basin_coord.append((x, y))
                        basin_nums.append(number + 1)

                elif y < len(height_list) - 1:

                    if height_list[y][x + 1] > number and \
                            height_list[y - 1][x] > number and \
                            height_list[y + 1][x] > number:
                        basin_coord.append((x, y))
                        basin_nums.append(number + 1)
                else:

                    if height_list[y][x + 1] > number and \
                            height_list[y - 1][x] > number:
                        basin_coord.append((x, y))
                        basin_nums.append(number + 1)

            elif x < len(each_line) - 1:

                if y == 0:
                    if height_list[y][x - 1] > number and \
                            height_list[y][x + 1] > number and \
                            height_list[y + 1][x] > number:
                        basin_coord.append((x, y))
                        basin_nums.append(number + 1)

                elif y < len(height_list) - 1:
                    if height_list[y][x - 1] > number and \
                            height_list[y][x + 1] > number and \
                            height_list[y - 1][x] > number and \
                            height_list[y + 1][x] > number:
                        basin_coord.append((x, y))
                        basin_nums.append(number + 1)

                elif y == len(height_list) - 1:
                    if height_list[y][x - 1] > number and \
                            height_list[y][x + 1] > number and \
                            height_list[y - 1][x] > number:
                        basin_coord.append((x, y))
                        basin_nums.append(number + 1)

            else:
                if y == 0:
                    if height_list[y][x - 1] > number and \
                            height_list[y + 1][x] > number:
                        basin_coord.append((x, y))
                        basin_nums.append(number + 1)

                elif y < len(height_list) - 1:
                    if height_list[y][x - 1] > number and \
                            height_list[y - 1][x] > number and \
                            height_list[y + 1][x] > number:
                        basin_coord.append((x, y))
                        basin_nums.append(number + 1)

                elif y == len(height_list) - 1:
                    if height_list[y][x - 1] > number and \
                            height_list[y - 1][x] > number:
                        basin_coord.append((x, y))
                        basin_nums.append(number + 1)

            x += 1
        y += 1

    return basin_coord, basin_nums


def check(x, y):
    global width, bottom, _map
    points = []
    x_temp = x
    y_temp = y

    while x_temp < width:
        x_temp += 1
        if _map[y_temp][x_temp] != 9:
            points.append((x_temp, y_temp))
        else:
            x_temp -= 1
            break

    x_temp = x
    y_temp = y
    while x_temp > 0:
        x_temp -= 1
        if _map[y_temp][x_temp] != 9:
            points.append((x_temp, y_temp))
        else:
            x_temp += 1
            break

    x_temp = x
    y_temp = y
    while y_temp > 0:
        y_temp -= 1
        if _map[y_temp][x_temp] != 9:
            points.append((x_temp, y_temp))
        else:
            y_temp += 1
            break

    x_temp = x
    y_temp = y
    while y_temp < bottom:
        y_temp += 1
        if _map[y_temp][x_temp] != 9:
            points.append((x_temp, y_temp))
        else:
            y_temp -= 1
            break

    return points


def basin_size(height_list, map_):
    global width, bottom, _map
    width = len(map_[1]) - 1
    bottom = len(map_) - 1
    _map = map_
    basin_sizes = []

    index = 0
    for basin in height_list:
        size = 0
        result = check(basin[0], basin[1])
        size += len(result)
        for point in result:
            new_result = check(point[0], point[1])
            for point in new_result:
                if point not in result:
                    result.append(point)
                    size += 1

        basin_sizes.append(size)
        index += 1

    basin_sizes.sort(reverse=True)

    return basin_sizes


def main():
    height_map = get_input()
    basin_points, basin_nums = find_lows(height_map)
    top_basin_sizes = basin_size(basin_points, height_map)

    product = top_basin_sizes[0] * top_basin_sizes[1] * top_basin_sizes[2]

    print("Part1 - Basin Sum:", sum(basin_nums))
    print()
    print("Part2 - Basin Size:", product)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()